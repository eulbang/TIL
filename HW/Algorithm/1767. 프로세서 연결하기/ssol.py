import sys
sys.stdin = open('sample_input.txt')

# 최대 전원 연결 코어 + 최소 전선 길이
# 코어의 위치를 배열로 만든 뒤 테두리에 있는 코어 제외 - 앞으로의 계산에 필요없음 - 최적화
# 테두리 제거한 배열을 DFS
# DFS 에서 상하좌우+패스 5가지 방향 보내기
# 상하좌우에서 전선 설치할 WIRE
# 설치 과정에서 장애물이 있을 경우 전선 회수
# 끝까지 설치했을 경우 회수하지 않고 연결된 코어 수 +1, 전선 길이 리턴
# DFS 에서 전원 연결 수 + 전선 길이 리턴하여 max(data, key=lambda x: (연결 코어 수, -전선 길이)) 활용

T = int(input())
for test_case in range(1, T + 1):
    # print(f'#{test_case} {}')