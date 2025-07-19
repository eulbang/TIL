import tkinter as tk

class SeatUI:
    def __init__(self, root, seat_manager, animation):
        self.root = root
        self.seat_manager = seat_manager
        self.animation = animation
        self.canvas = tk.Canvas(root, width=500, height=1050, bg='white')
        self.canvas.pack()
        self.root.after(20, self.update)

    def update(self):
        self.canvas.delete('all')
        # 좌석 그리기
        for idx, (x, y, r, c) in enumerate(self.animation.seat_positions):
            if self.seat_manager.seats[r][c] is None:
                color = '#bbb'
            elif self.seat_manager.seats[r][c] == "":
                color = '#fff'
            else:
                color = '#90caf9'
            # 좌석 높이/너비를 animation.py와 맞춤 (빈 공간 없이)
            seat_w = 500 / self.seat_manager.cols
            seat_h = (1050 * 0.18) / self.seat_manager.rows
            self.canvas.create_rectangle(x-seat_w/2, y-seat_h/2, x+seat_w/2, y+seat_h/2, fill=color, outline='#333')
            # 이름 표시
            if self.seat_manager.seats[r][c] not in (None, ""):
                self.canvas.create_text(x, y, text=self.seat_manager.seats[r][c], font=('Arial', 12, 'bold'))
        # 공 그리기
        for ball in self.animation.balls:
            if not ball.done:
                self.canvas.create_oval(ball.x-20, ball.y-20, ball.x+20, ball.y+20, fill=ball.color, outline='#333')
                self.canvas.create_text(ball.x, ball.y, text=ball.name, font=('Arial', 10, 'bold'))
        self.animation.step()
        self.root.after(20, self.update)
