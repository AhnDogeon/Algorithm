import sys
sys.stdin = open('13460_구슬탈출2.txt', 'r')

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(input()))



print('============디버깅============')
for i in range(N):
    for j in range(M):
        print(board[i][j], end=' ')
    print()
print('============디버깅============')

diff = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 북 : 0
# 동 : 1
# 남 : 2
# 서 : 3

B_visit = [[False] * M for _ in range(N)]
R_visit = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            R_index = [i, j]
        elif board[i][j] == 'B':
            B_index = [i, j]
        elif board[i][j] == 'O':
            hole = [i, j]
        else:
            R_visit[i][j] = True
            B_visit[i][j] = True

while True:
    for direc in diff:

