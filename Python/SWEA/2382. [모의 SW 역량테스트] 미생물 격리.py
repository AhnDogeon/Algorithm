T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    pan = [[[] for _ in range(N)] for _ in range(N)]
    # print(board)

    for i in range(K):
        col, row, number, direc = map(int, input().split())
        pan[col][row] = [number, direc]
    cnt = 0
    while cnt < M: # pan 은 원래 있는거 board 는 더해줘서 생성해줄것
        cnt += 1
        board = [[[] for _ in range(N)] for _ in range(N)]
        for a in range(N):
            for b in range(N):
                if len(pan[a][b]) > 0:
                    v = pan[a][b] # [ 리스트, 모양]
                    if v[1] == 1:
                        dx, dy = a - 1, b
                        if 0 <= dx < N and 0 <= dy < N:
                            if dx == 0 or dx == N - 1 or dy == 0 or dy == N - 1:# 벽부딪혔을 때!
                                board[dx][dy].append([v[0] // 2, 2])
                            else:
                                board[dx][dy].append([v[0], v[1]])
                    elif v[1] == 2:
                        dx, dy = a + 1, b
                        if 0 <= dx < N and 0 <= dy < N:
                            if dx == 0 or dx == N - 1 or dy == 0 or dy == N - 1:# 벽부딪혔을 때!
                                board[dx][dy].append([v[0] // 2, 1])
                            else:
                                board[dx][dy].append([v[0], v[1]])
                    elif v[1] == 3:
                        dx, dy = a, b - 1
                        if 0 <= dx < N and 0 <= dy < N:
                            if dx == 0 or dx == N - 1 or dy == 0 or dy == N - 1:# 벽부딪혔을 때!
                                board[dx][dy].append([v[0] // 2, 4])
                            else:
                                board[dx][dy].append([v[0], v[1]])
                    elif v[1] == 4:
                        dx, dy = a, b + 1
                        if 0 <= dx < N and 0 <= dy < N:
                            if dx == 0 or dx == N - 1 or dy == 0 or dy == N - 1:# 벽부딪혔을 때!
                                board[dx][dy].append([v[0] // 2, 3])
                            else:
                                board[dx][dy].append([v[0], v[1]])

        for m in range(N):
            for n in range(N):
                if len(board[m][n]) > 1:
                    hap = 0
                    result = 0
                    for i in board[m][n]:
                        if hap < i[0]:
                            direc = i[1]
                            hap = i[0]
                        result += i[0]
                    board[m][n] = [result, direc]
                elif len(board[m][n]) == 1:
                    board[m][n] = board[m][n][0]
        pan = board
    final_result = 0
    for i in range(N):
        for j in range(N):
            if len(pan[i][j]) > 0:
                final_result += pan[i][j][0]
    print('#{} {}'.format(test_case, final_result))