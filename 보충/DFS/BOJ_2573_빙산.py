import sys
sys.stdin = open('BOJ_2573_빙산.txt', 'r')

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]


for x in range(N):
    for y in range(M):
        if board[x][y]:
            visit[x][y] = True

ice_count = 0
time = 0

diff = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def DFS(n, m):
    stack = [[n, m]]
    while stack:
        s = stack.pop()
        for (a, b) in diff:
            dx, dy = s[0] + a, s[1] + b
            if 0 <= dx < N and 0 <= dy < M and board[dx][dy] != 0 and visit[dx][dy] == False:
                visit[dx][dy] = True
                stack.append([dx, dy])

def zero_count(i, j):
    zero = 0
    for (q, k) in diff:
        di, dj = i + q, j + k
        if board[di][dj] == 0:
            zero += 1
    return zero

flag = False
while True:
    for n in range(N):
        for m in range(M):
            if board[n][m] != 0 and visit[n][m] == False:
                visit[n][m] = True
                DFS(n, m)
                ice_count += 1

    if ice_count > 1:
        print(time)
        break

    else:
        copy_ice = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j]:
                    zero_cnt = zero_count(i, j)
                    if zero_cnt >= board[i][j]:
                        copy_ice[i][j] = 0
                    else:
                        copy_ice[i][j] = board[i][j] - zero_cnt
        for e in range(N):
            for f in range(M):
                board[e][f] = copy_ice[e][f]

        for e in range(N):
            for f in range(M):
                if board[e][f] != 0:
                    visit[e][f] = False
                    flag = True

        if flag == False:
            print(0)
            break
        time += 1
        ice_count = 0
        flag = False