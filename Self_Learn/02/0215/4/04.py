import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    maxH = 0
    minH = 0
    min_list = arr[0:0+M]
    for k in min_list:
        minH += k

    for i in range(len(arr)-M+1):
        add_list = arr[i:i+M]
        total = 0
        for j in add_list:
            total += j
        if total > maxH:
            maxH = total
        elif total < minH:
            minH = total
    result = maxH - minH
    print(f'#{test_case} {result}')