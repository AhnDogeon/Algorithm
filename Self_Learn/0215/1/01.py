import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxH = 0
    minH = arr[0]
    for i in arr:
        if i > maxH:
            maxH = i
        if i < minH:
        	minH = i
    print(f'#{test_case} {maxH-minH}')