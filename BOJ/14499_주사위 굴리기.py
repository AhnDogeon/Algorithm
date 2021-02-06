import sys
from copy import deepcopy
sys.stdin = open('14499_주사위 굴리기.txt', 'r')

N, M, x, y, K = map(int, input().split())


board = []
for _ in range(N):
    board_list = list(map(int, input().split()))
    board.append(board_list)

move = list(map(int, input().split()))
# print(move)
#
# print('===========디버깅=====================')
# for i in range(N):
#     for j in range(M):
#         print(board[i][j], end=' ')
#     print()
# print('=====================================')


up = 0
middle = 0
left = 0
right = 0
down = 0
bottom = 0


def RIGHT(a, b):
    global board, up, middle, left, right, down, bottom
    copy_up = deepcopy(up)
    copy_middle = deepcopy(middle)
    copy_left = deepcopy(left)
    copy_right = deepcopy(right)
    copy_down = deepcopy(down)
    copy_bottom = deepcopy(bottom)

    if board[a][b] == 0:
        up = copy_up
        middle = copy_left
        left = copy_bottom
        right = copy_middle
        down = copy_down
        bottom = copy_right
        board[a][b] = bottom
    else:
        up = copy_up
        middle = copy_left
        left = copy_bottom
        right = copy_middle
        down = copy_down
        bottom = board[a][b]
        board[a][b] = 0
    print(middle)


def LEFT(a, b):
    global board, up, middle, left, right, down, bottom
    copy_up = deepcopy(up)
    copy_middle = deepcopy(middle)
    copy_left = deepcopy(left)
    copy_right = deepcopy(right)
    copy_down = deepcopy(down)
    copy_bottom = deepcopy(bottom)

    if board[a][b] == 0:
        up = copy_up
        middle = copy_right
        left = copy_middle
        right = copy_bottom
        down = copy_down
        bottom = copy_left
        board[a][b] = bottom
    else:
        up = copy_up
        middle = copy_right
        left = copy_middle
        right = copy_bottom
        down = copy_down
        bottom = board[a][b]
        board[a][b] = 0
    print(middle)


def UP(a, b):
    global board, up, middle, left, right, down, bottom
    copy_up = deepcopy(up)
    copy_middle = deepcopy(middle)
    copy_left = deepcopy(left)
    copy_right = deepcopy(right)
    copy_down = deepcopy(down)
    copy_bottom = deepcopy(bottom)

    if board[a][b] == 0:
        up = copy_middle
        middle = copy_down
        left = copy_left
        right = copy_right
        down = copy_bottom
        bottom = copy_up
        board[a][b] = bottom
    else:
        up = copy_middle
        middle = copy_down
        left = copy_left
        right = copy_right
        down = copy_bottom
        bottom = board[a][b]
        board[a][b] = 0
    print(middle)


def DOWN(a, b):
    global board, up, middle, left, right, down, bottom
    copy_up = deepcopy(up)
    copy_middle = deepcopy(middle)
    copy_left = deepcopy(left)
    copy_right = deepcopy(right)
    copy_down = deepcopy(down)
    copy_bottom = deepcopy(bottom)

    if board[a][b] == 0:
        up = copy_bottom
        middle = copy_up
        left = copy_left
        right = copy_right
        down = copy_middle
        bottom = copy_down
        board[a][b] = bottom
    else:
        up = copy_bottom
        middle = copy_up
        left = copy_left
        right = copy_right
        down = copy_middle
        bottom = board[a][b]
        board[a][b] = 0
    print(middle)


for i in move:
    if i == 1:
        dx, dy = x, y + 1
        if 0 <= dx < N and 0 <= dy < M:
            RIGHT(dx, dy)
            x, y = dx, dy
    elif i == 2:
        dx, dy = x, y - 1
        if 0 <= dx < N and 0 <= dy < M:
            LEFT(dx, dy)
            x, y = dx, dy
    elif i == 3:
        dx, dy = x - 1, y
        if 0 <= dx < N and 0 <= dy < M:
            UP(dx, dy)
            x, y = dx, dy
    elif i == 4:
        dx, dy = x + 1, y
        if 0 <= dx < N and 0 <= dy < M:
            DOWN(dx, dy)
            x, y = dx, dy
    #
    # print('===========디버깅=====================')
    # for i in range(N):
    #     for j in range(M):
    #         print(board[i][j], end=' ')
    #     print()
    # print('=====================================')
    #

