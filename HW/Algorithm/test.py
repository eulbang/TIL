def dfs(diff, nums, last_num, res):
    global mx_num, mn_num

    if len(res) == k + 1:
        num = 0
        for d in res:
            num = num*10 + d
        mx_num = max(mx_num, num)
        mn_num = min(mn_num, num)
        return

    sign = diff[len(res)-1]
    if sign == '<':
        for i in nums:
            if i > last_num:
                next_nums = [x for x in nums if x != i]
                dfs(diff, next_nums, i, res+[i])
    else:
        for i in nums:
            if i < last_num:
                next_nums = [x for x in nums if x != i]
                dfs(diff, next_nums, i, res+[i])


k = int(input())
diff = input().split()
nums = list(range(10))
mx_num = -1
mn_num = 10**(k + 1)

for s in range(10):
    dfs(diff, [x for x in nums if x != s], s, [s])

print(str(mx_num).zfill(k + 1))
print(str(mn_num).zfill(k + 1))
