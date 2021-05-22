import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    l = int(P/P)
    r = P
    C = int((l+r)/2)
    count_A = 0
    while C != A:
        if C < A < r:
            r = r
            l = C
            C = int((C+r)/2)
            count_A += 1
        elif l < A < C:
            l = l
            r = C
            C = int((l+C)/2)
            count_A += 1

    l = int(P / P)
    r = P
    C = int((l + r) / 2)
    count_B = 0
    while C != B:
        if C < B < r:
            r = r
            l = C
            C = int((C+r)/2)
            count_B += 1
        elif l < B < C:
            l = l
            r = C
            C = int((l+C)/2)
            count_B += 1

    if count_A == count_B:
        print(f'#{test_case} {0}')
    elif count_A > count_B:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} A')