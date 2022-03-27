import sys
from copy import deepcopy
sys.stdin = open('12100_2048(EASY).txt', 'r')

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]


def up(up_board): # 1
    for i in range(1, N):
        for j in range(N):
            if up_board[i][j]:
                cnt = 0
                for a in range(i - 1, -1, -1):
                    if up_board[a][j] == 0:
                        cnt += 1
                up_board[i-cnt][j] = up_board[i][j]
                if cnt > 0:
                    up_board[i][j] = 0

    for i in range(1, N):
        for j in range(N):
            if up_board[i][j] == up_board[i-1][j]:
                up_board[i-1][j] += up_board[i][j]
                up_board[i][j] = 0

    for i in range(1, N):
        for j in range(N):
            if up_board[i][j]:
                cnt = 0
                for a in range(i - 1, -1, -1):
                    if up_board[a][j] == 0:
                        cnt += 1
                up_board[i-cnt][j] = up_board[i][j]
                if cnt > 0:
                    up_board[i][j] = 0
    return up_board

def down(down_board): # 2
    for i in range(N-2, -1, -1):
        for j in range(N):
            if down_board[i][j]:
                cnt = 0
                for a in range(i + 1, N):
                    if down_board[a][j] == 0:
                        cnt += 1
                down_board[i+cnt][j] = down_board[i][j]
                if cnt > 0:
                    down_board[i][j] = 0

    for i in range(N-1, 0, -1):
        for j in range(N):
            if down_board[i][j] == down_board[i-1][j]:
                down_board[i][j] += down_board[i-1][j]
                down_board[i-1][j] = 0

    for i in range(N - 2, -1, -1):
        for j in range(N):
            if down_board[i][j]:
                cnt = 0
                for a in range(i + 1, N):
                    if down_board[a][j] == 0:
                        cnt += 1
                down_board[i + cnt][j] = down_board[i][j]
                if cnt > 0:
                    down_board[i][j] = 0
    return down_board

def left(left_board): # 3
    for i in range(N):
        for j in range(1, N):
            if left_board[i][j]:
                cnt = 0
                for a in range(j - 1, -1, -1):
                    if left_board[i][a] == 0:
                        cnt += 1
                left_board[i][j-cnt] = left_board[i][j]
                if cnt > 0:
                    left_board[i][j] = 0

    for i in range(N):
        for j in range(1, N):
            if left_board[i][j] == left_board[i][j-1]:
                left_board[i][j-1] += left_board[i][j]
                left_board[i][j] = 0

    for i in range(N):
        for j in range(1, N):
            if left_board[i][j]:
                cnt = 0
                for a in range(j - 1, -1, -1):
                    if left_board[i][a] == 0:
                        cnt += 1
                left_board[i][j - cnt] = left_board[i][j]
                if cnt > 0:
                    left_board[i][j] = 0
    return left_board

def right(right_board): # 4
    for i in range(N):
        for j in range(N - 2, -1, -1):
            if right_board[i][j]:
                cnt = 0
                for a in range(j + 1, N):
                    if right_board[i][a] == 0:
                        cnt += 1
                right_board[i][j + cnt] = right_board[i][j]
                if cnt > 0:
                    right_board[i][j] = 0

    for i in range(N):
        for j in range(N - 1, 0, -1):
            if right_board[i][j] == right_board[i][j - 1]:
                right_board[i][j] += right_board[i][j - 1]
                right_board[i][j - 1] = 0

    for i in range(N):
        for j in range(N - 2, -1, -1):
            if right_board[i][j]:
                cnt = 0
                for a in range(j + 1, N):
                    if right_board[i][a] == 0:
                        cnt += 1
                right_board[i][j + cnt] = right_board[i][j]
                if cnt > 0:
                    right_board[i][j] = 0
    return right_board


direc = 4
direc_cnt = 5

selected = [[] for _ in range(direc_cnt)]


result = []
def full(depth):
    global result
    if direc_cnt == depth:
        direc_list = []
        for i in range(direc_cnt):
            direc_list.append(selected[i])
        result.append(direc_list)
    else:
        for j in range(1, direc + 1):
            selected[depth] = j
            full(depth+1)

full(0)

MAX = 0
for x in range(len(result)):
    copy_board = deepcopy(board)
    for y in range(len(result[x])):
        if result[x][y] == 1:
            copy_board = up(copy_board)
        elif result[x][y] == 2:
            copy_board = down(copy_board)
        elif result[x][y] == 3:
            copy_board = left(copy_board)
        elif result[x][y] == 4:
            copy_board = right(copy_board)
    for z in copy_board:
        if max(z) >= MAX:
            MAX = max(z)

print(MAX)