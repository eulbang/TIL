N, M, K = map(int, input().split())
nums = []
for _ in range(N):
    nums.append(int(input()))
control = []
for _ in range(M+K):
    control.append(list(map(int, input().split())))

for a, b, c in control:
    if a == 1:
        nums[b-1] = c
    else:
        print(sum(nums[b-1:c]))
