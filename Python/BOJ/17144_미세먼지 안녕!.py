import sys
sys.stdin = open('17144_미세먼지 안녕!.txt', 'r')

R, C, T = map(int, input().split())

board = []
dust_board = []
for i in range(R):
    board.append(list(map(int, input().split())))
    dust_board.append([0] * C)


diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dust(i, j):
    count = 0
    for (x, y) in diff:
        dx, dy = i + x, j + y
        if 0 <= dx < R and 0 <= dy < C and board[dx][dy] != -1:
            count += 1
            dust_board[dx][dy] = dust_board[dx][dy] + int(board[i][j] / 5)
    dust_board[i][j] -= int(board[i][j] / 5) * count


def clean(clean_list):
    global board
    cnt = 0
    for clean in clean_list: # 공기청정기 좌표
        dr, dc = clean[0], clean[1]
        if cnt == 1: # 밑에 공기청정기
            turn = False
            while True:
                if dr != R - 1 and dc != (C - 1) and turn == False:
                    dr += 1
                    if (dr - 1) == clean[0]:
                        board[dr][dc] = 0
                    else:
                        board[dr-1][dc] = board[dr][dc]
                        board[dr][dc] = 0
                elif dr == R - 1 and dc != (C - 1) and turn == False:
                    dc += 1
                    board[dr][dc-1] = board[dr][dc]
                    board[dr][dc] = 0
                elif dc == (C - 1) and dr != clean[0]:
                    dr -= 1
                    board[dr+1][dc] = board[dr][dc]
                    board[dr][dc] = 0
                elif dr == clean[0]:
                    dc -= 1
                    if board[dr][dc] != -1:
                        board[dr][dc+1] = board[dr][dc]
                        board[dr][dc] = 0
                        turn = True
                if dr == clean[0] and dc == clean[1]:
                    break
        elif cnt == 0:
            turn = False
            while True:
                if dr != 0 and dc != (C - 1) and turn == False:
                    dr -= 1
                    if (dr + 1) == clean[0]:
                        board[dr][dc] = 0
                    else:
                        board[dr+1][dc] = board[dr][dc]
                        board[dr][dc] = 0
                elif dr == 0 and dc != (C - 1) and turn == False:
                    dc += 1
                    board[dr][dc-1] = board[dr][dc]
                    board[dr][dc] = 0
                elif dc == (C - 1) and dr != clean[0]:
                    dr += 1
                    board[dr-1][dc] = board[dr][dc]
                    board[dr][dc] = 0
                elif dr == clean[0]:
                    dc -= 1
                    if board[dr][dc] != -1:
                        board[dr][dc+1] = board[dr][dc]
                        board[dr][dc] = 0
                        turn = True
                if dr == clean[0] and dc == clean[1]:
                    break
            cnt += 1

for x in range(T):
    # print(x, end='')
    # print('번째 확산 전=======================')
    # for i in range(R):
    #     for j in range(C):
    #         print(board[i][j], end=' ')
    #     print()
    # print('========================')

    clean_list = []
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                dust(i, j)
            elif board[i][j] == -1:
                clean_list.append([i, j])

    for i in range(R):
        for j in range(C):
            board[i][j] += dust_board[i][j]
    # print(x, end='')
    # print('번째 확산 후=======================')
    # for i in range(R):
    #     for j in range(C):
    #         print(board[i][j], end=' ')
    #     print()
    # print('========================')

    clean(clean_list)
    dust_board = []
    for i in range(R):
        dust_board.append([0] * C)
    # print(x, end='')
    # print('번째 청소 후=======================')
    # for i in range(R):
    #     for j in range(C):
    #         print(board[i][j], end=' ')
    #     print()
    # print('========================')
    #


total = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            total += board[i][j]

print(total)