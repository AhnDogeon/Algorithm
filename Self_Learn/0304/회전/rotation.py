import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(len(arr)):
        if M % N == i:
            print(f'#{test_case} {arr[i]}')
