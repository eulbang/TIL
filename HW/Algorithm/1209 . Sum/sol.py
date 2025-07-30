import sys
# open을 사용해서 input 파일을 연다
sys.stdin = open('input.txt')
# sys.setrecursionlimit(10000)

for _ in range(10): # 테스트케이스 수
    tc = input() # 테스트케이스 번호 입력
    # 입력 받은 문자열을 공백 기준으로 쪼개서 정수로 바꾼다음 리스트에 담는걸 100번반복
    data = [list(map(int, input().split())) for _ in range(100)]
    # print(data)
    # 각 행마다 가진 값들을 더한다.
    # 각 열마다 가진 값들을 더한다.
    # 대각선의 값들을 더한다.
    # 그 모든 값들 중 제일 큰 값을 구한다. -> max 금지
    
    # 100 X 100을 2차원 리스트로 받아야 한다.
    # 즉 , 한 번 입력받은 한 줄에 100개의 숫자가 공백을 기준으로 문자열로 오게 됨
        # 이걸 100번 반복해야함.
    # data = []   # 2차원 배열을 만들기 위한 리스트
    # for _ in range(100):
    #     # 공백 기준으로 쪼개진 문자열 (ex '13', '24')를 정수로 바꿔야 함
    #     tmp_list = input().split()  # 공백 기준으로 쪼개서 리스트로 만듬
    #     map_data = map(int, tmp_list)   # 리스트로 만들어야함
    #     map_to_list_data = list(map_data)
    #     # data.append(tmp_list)   # 그 리스트를 data에 추가
    #     data.append(map_to_list_data)
    # print(data)

    def row_max(row_idx, mx):
        if row_idx >= len(data):
            return mx
        sm = row_sum(row_idx, 0, 0)
        if sm > mx:
            mx = sm
        return row_max(row_idx + 1, mx)

    def row_sum(x, y, sm):
        if y >= len(data[0]):
            return sm
        return row_sum(x, y + 1, sm + data[x][y])

    def col_max(col_idx, mx):
        if col_idx >= len(data[0]):
            return mx
        sm = col_sum(0, col_idx, 0)
        if sm > mx:
            mx = sm
        return col_max(col_idx + 1, mx)

    def col_sum(x, y, sm):
        if x >= len(data):
            return sm
        return col_sum(x + 1, y, sm + data[x][y])

    def down_max(start_row, mx):
        if start_row >= len(data):
            return mx
        sm = down_sum(start_row, 0, 0)
        if sm > mx:
            mx = sm
        return down_max(start_row + 1, mx)

    def down_sum(x, y, sm):
        if x >= len(data) or y >= len(data[0]):
            return sm
        return down_sum(x + 1, y + 1, sm + data[x][y])

    def up_max(start_row, mx):
        if start_row < 0:
            return mx
        sm = up_sum(start_row, 0, 0)
        if sm > mx:
            mx = sm
        return up_max(start_row - 1, mx)

    def up_sum(x, y, sm):
        if x < 0 or y >= len(data[0]):
            return sm
        return up_sum(x - 1, y + 1, sm + data[x][y])

    def data_max():
        r = row_max(0, 0)
        c = col_max(0, 0)
        d1 = down_max(0, 0)
        d2 = up_max(len(data) - 1, 0)

        if r > c:
            bigger1 = r
        else:
            bigger1 = c

        if d1 > d2:
            bigger2 = d1
        else:
            bigger2 = d2

        if bigger1 > bigger2:
            return bigger1
        else:
            return bigger2

    print(f"#{tc} {data_max()}")

