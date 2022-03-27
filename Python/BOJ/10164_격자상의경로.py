diff = [(0, 1), (1, 0)]
def DP(x, y, N, M, board):
    if x == N - 1 and y == M - 1:
        return
    for (a, b) in diff:
        dx, dy = x + a, y + b
        if 0 <= dx < N and 0 <= dy < M:
            if dx == 0:
                board[dx][dy] = 1
                DP(dx, dy, N, M, board)
            if dy == 0:
                board[dx][dy] = 1
                DP(dx, dy, N, M, board)
            elif dx != 0 and dy != 0:
                board[dx][dy] = board[dx-1][dy] + board[dx][dy - 1]
                DP(dx, dy, N, M, board)


N, M, K = map(int, input().split())

tmp = 1
arr = []
for i in range(N):
    lst = []
    for j in range(M):
        lst.append(tmp)
        tmp += 1
    arr.append(lst)

for i in range(N):
    for j in range(M):
        if arr[i][j] == K:
            Ki = i
            Kj = j
            break

if K == 0:
    board = [[0 for _ in range(M)] for _ in range(N)]
    board[0][0] = 1
    DP(0, 0, N, M, board)
    print(board[N-1][M-1])

else:
    board = [[0 for _ in range(Kj + 1)] for _ in range(Ki + 1)]
    board[0][0] = 1
    DP(0, 0, Ki + 1, Kj + 1, board)
    result1 = board[Ki][Kj]

    board = [[0 for _ in range(M - Kj)] for _ in range(N-Ki)]
    board[0][0] = 1
    DP(0, 0, N - Ki, M - Kj, board)
    result2 = board[N-Ki-1][M-Kj-1]
    print(result1 * result2)
