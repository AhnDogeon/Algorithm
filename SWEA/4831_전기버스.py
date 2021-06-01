import sys
sys.stdin = open('4831_전기버스.txt', 'r')

T = int(input())


def Bus(start, end, oil, cnt):
    if start + oil >= end:
        return cnt
    else:
        max_distance = 0
        for i in range(start + 1, start + oil + 1):
            if board[i] == True:
                max_distance = i
        if max_distance == 0:
            return 0
        else:
            return Bus(max_distance, end, oil, cnt + 1)



for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    board = [False] * (N + 1)
    for j in range(len(arr)):
        board[arr[j]] = True
    start = 0
    end = N
    print('#{} {}'.format(test_case, Bus(start, end, K, 0)))