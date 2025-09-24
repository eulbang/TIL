import sys
input = sys.stdin.readline

def lower_bound(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def upper_bound(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def ceil_div(a, b):
    return -((-a) // b)

def count_leq(x, A, B):
    m = len(B)
    cnt = 0
    for a in A:
        if a > 0:
            t = x // a
            cnt += upper_bound(B, t)
        elif a == 0:
            if x >= 0:
                cnt += m
        else:
            t = ceil_div(x, a)
            idx = lower_bound(B, t)
            cnt += m - idx
    return cnt

first = list(map(int, input().split()))
if len(first) == 3:
    n, m, k = first
else:
    n, k = first
    m = n

A = []
while len(A) < n:
    A += list(map(int, input().split()))
B = []
while len(B) < m:
    B += list(map(int, input().split()))

A.sort()
B.sort()

a_min, a_max = A[0], A[-1]
b_min, b_max = B[0], B[-1]
cands = [a_min*b_min, a_min*b_max, a_max*b_min, a_max*b_max]
lo, hi = min(cands), max(cands)

while lo < hi:
    mid = (lo + hi) // 2
    if count_leq(mid, A, B) >= k:
        hi = mid
    else:
        lo = mid + 1

print(lo)
