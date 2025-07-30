import sys
# open을 사용해서 input 파일을 연다
sys.stdin = open('sample_input.txt')

for _ in range(3): # 테스트케이스 수
    tc = input() # 테스트케이스 번호 입력