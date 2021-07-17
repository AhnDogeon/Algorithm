from collections import deque

M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(arr):
    Q = deque()
    for i in arr:
        Q.append(i)
    day = -1
    while Q:
        for _ in range(len(Q)):
            v = Q.popleft()
            for (a, b) in diff:
                dx = v[0] + a
                dy = v[1] + b
                if dx == N or dx < 0 or dy == M or dy < 0:
                    continue
                elif board[dx][dy] == 0 and visit[dx][dy] == False:
                    visit[dx][dy] = True
                    board[dx][dy] = 1
                    Q.append([dx, dy])
        day += 1

    for x in range(N):
        for y in range(M):
            if visit[x][y] == False:
                return  -1
    else:
        return day



start = []
no = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            start += [[i, j]]
        elif board[i][j] == -1:
            no += [[i, j]]

visit = [[False] * M for _ in range(N)]

for a in range(len(start)):
    visit[start[a][0]][start[a][1]] = True

for b in range(len(no)):
    visit[no[b][0]][no[b][1]] = True


print(BFS(start))