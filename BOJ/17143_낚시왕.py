import sys
import copy
sys.stdin = open('17143_낚시왕.txt', 'r')
# 동, 서, 남, 북 방향 좌표 정하기부터 시작입니다. v 부터

R, C, M = map(int, input().split())

shark = 0

board = []
for i in range(R):
    line = []
    for j in range(C):
        info = [0, 0, 0]
        line.append(info)
    board.append(line)

if M:
    for setting in range(M):
        r, c, s, d, z = map(int, input().split())
        board[r-1][c-1][0] = s
        board[r-1][c-1][1] = d
        board[r-1][c-1][2] = z
else:
    print(0)

#
# # 디버깅-----------------
# for a in range(R):
#     for b in range(C):
#         print(board[a][b], end=' ')
#     print()
# # 디버깅-----------------

def catch(x):
    global shark
    for y in range(R):
        if board[y][x][2]:
            shark += board[y][x][2]
            board[y][x] = [0, 0, 0]
            break

def move(board, copy_board):
    for i in range(R):
        for j in range(C):
            current_i = i
            current_j = j
            if board[i][j][2]:
                if board[i][j][1] == 1:
                    v = board[i][j][0] # 몇 칸 이동해야하는지
                    while v:
                        if v - current_i >= 0:
                            v = v - current_i
                            current_i = 0
                            board[i][j][1] = 2
                            if v == 0:
                                # board[i][j][1] = 1
                                break
                        else:
                            current_i = current_i - v
                            v = 0
                            break
                        if v - (R - 1) >= 0:
                            v = v - (R - 1)
                            current_i = R - 1
                            board[i][j][1] = 1
                            if v == 0:
                                # board[i][j][1] = 2
                                break
                        else:
                            current_i = v
                            break
                elif board[i][j][1] == 2:
                    v = board[i][j][0] # 몇 칸 이동해야하는지
                    while v:
                        if v - (R - 1 - current_i) >= 0:
                            v = v - (R - 1 - current_i)
                            current_i = R - 1
                            board[i][j][1] = 1
                            if v == 0:
                                # board[i][j][1] = 2
                                break
                        else:
                            current_i = current_i + v
                            v = 0
                            break
                        if v - (R - 1) >= 0:
                            v = v - (R - 1)
                            current_i = 0
                            board[i][j][1] = 2
                            if v == 0:
                                # board[i][j][1] = 1
                                break
                        else:
                            current_i = R - 1 - v
                            break
                elif board[i][j][1] == 3:
                    v = board[i][j][0] # 몇 칸 이동해야하는지
                    while v:
                        if v - (C - 1 - current_j) >= 0:
                            v = v - (C - 1 - current_j)
                            current_j = C - 1
                            board[i][j][1] = 4
                            if v == 0:
                                # board[i][j][1] = 3
                                break
                        else:
                            current_j = current_j + v
                            v = 0
                            break
                        if v - (C - 1) >= 0:
                            v = v - (C - 1)
                            current_j = 0
                            board[i][j][1] = 3
                            if v == 0:
                                # board[i][j][1] = 4
                                break
                        else:
                            current_j = current_j - v
                            break
                elif board[i][j][1] == 4:
                    v = board[i][j][0] # 몇 칸 이동해야하는지
                    while v:
                        if v - current_j >= 0:
                            v = v - current_j
                            current_j = 0
                            board[i][j][1] = 3
                            if v == 0:
                                # board[i][j][1] = 4
                                break
                        else:
                            current_j = current_j - v
                            v = 0
                            break
                        if v - (C - 1) >= 0:
                            v = v - (C - 1)
                            current_j = C - 1
                            board[i][j][1] = 4
                            if v == 0:
                                # board[i][j][1] = 3
                                break
                        else:
                            current_j = v
                            break
                if copy_board[current_i][current_j] == [0, 0, 0]:
                    copy_board[current_i][current_j] = board[i][j]
                else:
                    if copy_board[current_i][current_j][2] < board[i][j][2]:
                        copy_board[current_i][current_j] = board[i][j]
                    else:
                        pass
                board[i][j] = [0, 0, 0]

if M:
    for x in range(C):
        catch(x) # 잡는함수()
        copy_board = []
        for i in range(R):
            line = []
            for j in range(C):
                info = [0, 0, 0]
                line.append(info)
            copy_board.append(line)
        move(board, copy_board) # 상어이동함수()
        # print('=================이동후==========================')
        board = copy.deepcopy(copy_board)
        # 디버깅-----------------
        # for a in range(R):
        #     for b in range(C):
        #         print(board[a][b], end=' ')
        #     print()
        # # 디버깅-----------------
        # print('===========================================')

    print(shark)