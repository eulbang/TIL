import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

res = 0
i = 0
j = N - 1

while i + 1 <= j and nums[i] < 1:
    if nums[i] < 0 and nums[i+1] < 0:
        res += nums[i] * nums[i+1]
        i += 2
    elif nums[i] < 0 and nums[i+1] == 0:
        i += 2
    else:
        break

if i <= j and nums[i] < 0:
    res += nums[i]
    i += 1

while i <= j and nums[i] == 0:
    i += 1

while i <= j and nums[i] == 1:
    res += 1
    i += 1

while i + 1 <= j:
    res += nums[j] * nums[j-1]
    j -= 2

if i == j:
    res += nums[i]

print(res)
