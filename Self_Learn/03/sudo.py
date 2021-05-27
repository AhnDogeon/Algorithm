import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    if 0 < W <= R:
        if Q > (P * W):
            print(f'#{test_case} {P * W}')
        else:
            print(f'#{test_case} {Q}')
    else:
        if (S * (W - R) + Q) > (P * W):
            print(f'#{test_case} {P * W}')
        else:
            print(f'#{test_case} {S * (W - R) + Q}')
