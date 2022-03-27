import sys
sys.stdin = open('6913_동철이의 프로그래밍 대회.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]


    MAX = 0
    MAX_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
        else:
            if cnt > MAX:
                MAX = cnt
                MAX_cnt = 1
            elif cnt == MAX:
                MAX = cnt
                MAX_cnt += 1
            else:
                pass
    print('#{} {} {}'.format(test_case, MAX_cnt, MAX))