# import sys
# sys.stdin = open('2605_캔디팡(BFS).txt', 'r')
#
# board = [list(map(int, input().split())) for _ in range(7)]
# visit = [[False] * 7 for _ in range(7)]
#
#
# diff = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# total = 0
# def BFS(x, y, value):
#     global total
#     time = 0
#     Que = [[x, y]]
#     while Que:
#         v = Que.pop(0)
#         visit[v[0]][v[1]] = True
#         for (a, b) in diff:
#             dx, dy = v[0] + a, v[1] + b
#             if 0 <= dx < 7 and 0 <= dy < 7 and visit[dx][dy] == False and board[dx][dy] == value:
#                 visit[dx][dy] = True
#                 time += 1
#                 Que.append([dx, dy])
#     if time >= 2:
#         total += 1
#     print('=============디버깅================')
#     print('total은', total, '숫자는', value)
#     for c in range(7):
#         for d in range(7):
#             print(visit[c][d], end=' ')
#         print()
#     print('===================================')
#
# for i in range(7):
#     for j in range(7):
#         if visit[i][j] != True:
#             BFS(i, j, board[i][j])
# print(total)


import sys
sys.stdin = open('2605_캔디팡(BFS).txt', 'r')

board = []

for _ in range(7):
    board.append(list(map(int, input().split())))

visit = [[False] * 7 for _ in range(7)]

total = 0

diff = [(0, 1),(1,0),(-1,0),(0,-1)]
def BFS(x, y, value):
    global total
    time = 0
    Que = [[x, y]]

    while Que:
        v = Que.pop(0)
        visit[v[0]][v[1]] = True
        for a, b in diff:
            dx, dy = v[0] + a, v[1] + b
            if 0 <= dx < 7 and 0<= dy < 7 and visit[dx][dy] != True and board[dx][dy] == value:
                time += 1
                Que.append([dx, dy])
    if time >= 2:
        total += 1

for i in range(7):
    for j in range(7):
        BFS(i, j, board[i][j])


print(total)