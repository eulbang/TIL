import sys
sys.stdin = open('sample_input.txt')


def prefix_function(p):
    m = len(p)
    pi = [0]*m
    j = 0
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def count_kmp(text, pat):
    pi = prefix_function(pat)
    n, m = len(text), len(pat)
    j = 0
    cnt = 0
    for i in range(n):
        while j > 0 and text[i] != pat[j]:
            j = pi[j-1]
        if text[i] == pat[j]:
            j += 1
            if j == m:
                cnt += 1
                j = pi[j-1]
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    bok = input()
    wrd = input()

    print(f"#{test_case} {count_kmp(bok, wrd)}")
