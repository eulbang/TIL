import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    stick = list(input())

    stack, sm = 0, 0
    for i in range(len(stick)):
        if stick[i] == ')' and stick[i-1] == '(':
            pass
        elif stick[i] == '(' and stick[i+1] == ')':
            sm += stack
        elif stick[i] == '(':
            stack += 1
        elif stick[i] == ')':
            sm += 1
            stack -= 1

    print(f"{test_case} {sm}")