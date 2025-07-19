import random
import math

class Ball:
    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(2, 4)
        self.done = False
        self.seat_idx = None
        self.stuck_time = 0
        self.last_x = x

class BallAnimation:
    def _apply_shockwave(self, cx, cy, power=30, radius=120):
        for ball in self.balls:
            if ball.done:
                continue
            dx = ball.x - cx
            dy = ball.y - cy
            dist = (dx**2 + dy**2)**0.5
            if dist < radius and dist > 0:
                fx = dx / dist * power * random.uniform(0.8, 1.2)
                fy = dy / dist * power * random.uniform(0.8, 1.2)
                ball.vx += fx
                ball.vy += fy
    def __init__(self, seat_manager, students):
        self.seat_manager = seat_manager
        self.students = students
        self.balls = []
        self.seat_positions = self._calc_seat_positions()
        self._init_balls()

    def _calc_seat_positions(self):
        # 좌석 위치 계산 (하단에 딱 붙게, 빈 공간 없이)
        positions = []
        width, height = 500, 1050
        seat_w = width / self.seat_manager.cols
        seat_h = (height * 0.18)  # 좌석 영역을 전체의 18%로 낮춤
        seat_h_unit = seat_h / self.seat_manager.rows
        y0 = height - seat_h
        for r in range(self.seat_manager.rows):
            for c in range(self.seat_manager.cols):
                x = seat_w/2 + c*seat_w
                y = y0 + seat_h_unit/2 + r*seat_h_unit
                positions.append((x, y, r, c))
        return positions

    def _init_balls(self):
        colors = self._gen_colors(len(self.students))
        for i, name in enumerate(self.students):
            self.balls.append(Ball(name, colors[i], 250, 40))

    def _gen_colors(self, n):
        import colorsys
        return [
            '#%02x%02x%02x' % tuple(int(c*255) for c in colorsys.hsv_to_rgb(i/n, 0.6, 1.0))
            for i in range(n)
        ]

    def step(self):
        # 물리 엔진: 중력, 충돌, 좌석 할당, 공끼리 겹침 방지, 화면 밖 방지
        gravity = 0.5 * 0.666  # 150% 느리게
        width, height = 500, 1050
        radius = 20
        for ball in self.balls:
            if ball.done:
                continue
            ball.vy += gravity
            ball.x += ball.vx
            ball.y += ball.vy
            # 화면 밖 방지
            if ball.x < radius:
                ball.x = radius
                ball.vx = abs(ball.vx) * 0.5
            if ball.x > width - radius:
                ball.x = width - radius
                ball.vx = -abs(ball.vx) * 0.5
            if ball.y < radius:
                ball.y = radius
                ball.vy = abs(ball.vy) * 0.5
            if ball.y > height - radius:
                ball.y = height - radius
                ball.vy = -abs(ball.vy) * 0.5
            # 3초 이상 수직으로 같은 위치에 있으면 충격파
            if abs(ball.x - ball.last_x) < 2:
                ball.stuck_time += 1
            else:
                ball.stuck_time = 0
                ball.last_x = ball.x
            if ball.stuck_time > 150:  # 3초(20ms*150)
                shock_x = ball.x + random.uniform(-40, 40)
                shock_y = ball.y + random.uniform(-40, 40)
                self._apply_shockwave(shock_x, shock_y)
                ball.stuck_time = 0
        for i, a in enumerate(self.balls):
            if a.done:
                continue
            for j, b in enumerate(self.balls):
                if i >= j or b.done:
                    continue
                dx = a.x - b.x
                dy = a.y - b.y
                dist = (dx**2 + dy**2)**0.5
                min_dist = 2*radius
                if dist < min_dist and dist > 0:
                    push = (min_dist - dist) / 2
                    a.x += dx/dist * push
                    a.y += dy/dist * push
                    b.x -= dx/dist * push
                    b.y -= dy/dist * push
        # 좌석 충돌 및 할당
        # 좌석 할당 우선순위: 아래 행이 모두 할당/비활성화된 경우에만 위 행 할당
        # 1. 할당 가능한 행 찾기
        rows = self.seat_manager.rows
        cols = self.seat_manager.cols
        seats = self.seat_manager.seats
        assignable_row = rows - 1
        for r in range(rows-1, -1, -1):
            row_full = True
            for c in range(cols):
                if seats[r][c] == "":
                    row_full = False
                # 비활성화(None)는 무시
            if not row_full:
                assignable_row = r
                break
        # 2. 좌석 충돌 및 할당
        for ball in self.balls:
            if ball.done:
                continue
            for idx, (sx, sy, r, c) in enumerate(self.seat_positions):
                # 좌석/공 테두리 기준 충돌
                seat_w = 500 / self.seat_manager.cols
                seat_h = (700 * 0.18) / self.seat_manager.rows
                half_w = seat_w / 2
                half_h = seat_h / 2
                radius = 20
                dx = abs(ball.x - sx)
                dy = abs(ball.y - sy)
                # 충돌: 공의 테두리와 좌석의 테두리가 닿는 경우
                collide_x = dx < (half_w + radius)
                collide_y = dy < (half_h + radius)
                collide = collide_x and collide_y
                if seats[r][c] is None or not self.seat_manager.is_empty(r, c):
                    if collide:
                        # 튕김 방향 보정
                        if dx > dy:
                            ball.vx *= -0.7
                        else:
                            ball.vy *= -0.7
                        ball.x += random.uniform(-5, 5)
                        ball.y -= 10
                    continue
                # 할당은 아래 좌석이 비어있지 않을 때만(맨 아래는 바로 할당)
                can_assign = False
                if r == self.seat_manager.rows - 1:
                    can_assign = True
                else:
                    below = self.seat_manager.seats[r+1][c]
                    if below is None or below != "":
                        can_assign = True
                if can_assign and collide:
                    self.seat_manager.assign(r, c, ball.name)
                    ball.x, ball.y = sx, sy
                    ball.done = True
                    ball.seat_idx = idx
                    break
