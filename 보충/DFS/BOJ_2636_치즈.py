import sys
sys.setrecursionlimit(100000)
sys.stdin = open('BOJ_2636_치즈.txt', 'r')

R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(list(map(int, input().split())))


def create_visit():
    visit = []
    for r in range(R):
        visit_list = []
        for c in range(C):
            if board[r][c] == 1:
                visit_list.append(True)
            elif board[r][c] == 0:
                visit_list.append(False)
        visit.append(visit_list)
    return visit


diff = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def DFS(a, b):
    global count
    if board[a][b] == 0 and visit[a][b] == False:
        visit[a][b] = True
        for (i, j) in diff:
            da, db = a + i, b + j
            if 0 <= da < R and 0 <= db < C:
                if board[da][db] == 1:
                    board[da][db] = 0
                    count += 1
                DFS(da, db)


final_count = 0xfff
time = 0
while final_count:
    time += 1
    visit = create_visit()
    count = 0
    DFS(0, 0)
    # print('====디버깅=======================')
    # print(count)
    # print(time)
    # for x in range(R):
    #     for y in range(C):
    #         print(board[x][y], end=' ')
    #     print()
    # print('====디버깅=======================')
    if count == 0:
        print(time - 1)
        print(final_count)
        break
    else:
        final_count = count
