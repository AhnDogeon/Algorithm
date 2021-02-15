import sys
sys.stdin = open('14500_테트로미노.txt', 'r')
N, M = map(int, input().split())
board = []
for a in range(N):
    insert_board = list(map(int, input().split()))
    board.append(insert_board)


MAX = 0
diff = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def DFS(i, j, total, cnt):
    global MAX, board
    if cnt == 4:
        if total >= MAX:
            MAX = total
    elif cnt < 4:
        for (a, b) in diff:
            dx, dy = i + a, j + b
            if 0 <= dx < N and 0 <= dy < M and visit[dx][dy] == False:
                visit[dx][dy] = True
                DFS(dx, dy, total + board[dx][dy], cnt + 1)
                visit[dx][dy] = False



middle_diff = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def middle(i, j, total2):
    global MAX
    result = []
    for (x, y) in middle_diff:
        dx, dy = i + x, j + y
        if 0 <= dx < N and 0 <= dy < M:
            result.append(board[dx][dy])
    if len(result) >= 3:
        total2 += result.pop(result.index(max(result)))
        total2 += result.pop(result.index(max(result)))
        total2 += result.pop(result.index(max(result)))
        if total2 >= MAX:
            MAX = total2


for i in range(N):
    for j in range(M):
        visit = [[False] * M for _ in range(N)]
        visit[i][j] = True
        DFS(i, j, board[i][j], 1)
        middle(i, j, board[i][j])
print(MAX)