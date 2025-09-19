ipt = input()

lst = [int(ipt[0])]
for i in range(1, len(ipt)):
    try:
        try:
            int(ipt[i])
            lst[len(lst) - 1] = lst[len(lst) - 1] * 10 + int(ipt[i])
        except TypeError:
            lst.append(int(ipt[i]))
    except ValueError:
        lst.append(ipt[i])

i = 1
while i < len(lst):
    if lst[i] == '+':
        lst[i-1] += lst[i+1]
        lst.pop(i)
        lst.pop(i)
        continue
    i += 2

while True:
    try:
        lst.remove(None)
    except ValueError:
        break

res = lst[0]
for i in range(2, len(lst), 2):
    res -= lst[i]

print(res)