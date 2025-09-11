import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()

result = []
answers = set()

def func(now, cnt):
    if cnt == M:
        answers.add(tuple(N_list[p] for p in result))  # ← 문자열 대신 튜플
        return
    for idx in range(now, len(N_list)):  # 순열: 매 단계 전체 탐색
        if idx in result:           # 같은 인덱스 재사용 금지(간단 버전)
            continue
        result.append(idx)
        func(idx, cnt + 1)          # now는 사실상 의미 없음 (최소수정 유지)
        result.pop()

func(0, 0)

# 튜플은 숫자 기준 사전순으로 정렬됨
for seq in sorted(answers):
    print(' '.join(map(str, seq)))
