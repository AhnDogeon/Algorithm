import sys
sys.stdin = open('2610_그림판 채우기(BFS).txt', 'r')



diff = [(-1, 0),(0, 1),(1, 0),(0, -1)]

def BFS(a, b):
    Que = [[a, b]]
    visit[a][b] = True
    board[a][b] = '*'
    while Que:
        v = Que.pop(0)
        for (c, d) in diff:
            da, db = v[0] + c, v[1] + d
            if 0 <= da < 10 and 0 <= db < 10 and visit[da][db] == False and board[da][db] == '_':
                board[da][db] = '*'
                visit[da][db] = True
                Que.append([da, db])


board = [list(input()) for _ in range(10)]
visit = [[False] * 10 for _ in range(10)]
x, y = map(int, input().split())

if board[y][x] == '_':
    BFS(y, x)

for i in range(10):
    for j in range(10):
        print(board[i][j], end= '')
    print()