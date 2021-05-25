import sys
from copy import deepcopy
sys.stdin = open('17406_배열 돌리기4.txt', 'r')

maxhap = 0xffff
N, M, K = map(int, input().split())

copy_board = []
for _ in range(N):
    copy_board.append(list(map(int, input().split())))



k_list = []
for _ in range(K):
    k_list.append(list(map(int, input().split())))


def dol(board, start, end):
    if start == end:
        return
    else:
        x = start[0]
        y = start[1]
        tmp = board[x][y]
        while True:
            if y != end[1]:
                tmp, board[x][y+1] = board[x][y + 1], tmp
                y += 1
            else:
                break
        while True:
            if x != end[0]:
                tmp, board[x+1][y] = board[x+1][y], tmp
                x += 1
            else:
                break
        while True:
            if y != start[1]:
                tmp, board[x][y - 1] = board[x][y - 1], tmp
                y -= 1
            else:
                break
        while True:
            if x != start[0]:
                tmp, board[x - 1][y] = board[x-1][y], tmp
                x -= 1
            else:
                break

        return dol(board, [start[0]+1, start[1]+1], [end[0] - 1, end[1]-1])


def hap(board):
    global maxhap
    for a in range(len(board)):
        total = 0
        for b in range(len(board[a])):
            total += board[a][b]
        if total <= maxhap:
            maxhap = total

def perm(k, n):
    if k == n:
        # print(k_list)
        board = deepcopy(copy_board)
        for yeon in k_list:
            minus_low = yeon[0] - yeon[2] - 1
            minus_high = yeon[1] - yeon[2] - 1
            plus_low = yeon[0] + yeon[2] - 1
            plus_high = yeon[1] + yeon[2] - 1

            start = [minus_low, minus_high]
            end = [plus_low, plus_high]

            dol(board, start, end)
        # for c in range(len(board)):
        #     for d in range(len(board[c])):
        #         print(board[c][d], end=' ')
        #     print()
        hap(board)
        # print(maxhap)
        # print('=========================================')
        return

    for i in range(k, n):
        k_list[i], k_list[k] = k_list[k], k_list[i]
        perm(k + 1, n)
        k_list[i], k_list[k] = k_list[k], k_list[i]

perm(0, len(k_list))
print(maxhap)
