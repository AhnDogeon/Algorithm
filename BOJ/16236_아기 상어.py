import sys
sys.stdin = open('16236_아기 상어.txt', 'r')

N = int(input())

board = []
for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)

size = 2
move = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            current_i = i
            current_j = j

diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def BFS(current_i, current_j, catch):
    visit = [[False] * N for _ in range(N)]
    Dis = [[0] * N for _ in range(N)]
    Que = [[current_i, current_j]]
    while Que:
        v = Que.pop(0)
        for (x, y) in diff:
            dx, dy = v[0]+ x, v[1] + y
            if 0 <= dx < N and 0 <= dy < N and visit[dx][dy] == False and board[dx][dy] <= size:
                visit[dx][dy] = True
                Dis[dx][dy] = Dis[v[0]][v[1]] + 1
                Que.append([dx, dy])
                if 0 < board[dx][dy] < size:
                    catch.append([dx, dy, Dis[dx][dy]])
    return catch


catch = [1]
eat = 0
while catch:
    catch = []
    catch = BFS(current_i, current_j, catch)
    if catch:
        if len(catch) >= 2:
            dis_min = 0xffff
            for i in range(len(catch)):
                if dis_min > catch[i][2]:
                    dis_min = catch[i][2]

            dis_catch = []
            for j in range(len(catch)):
                if catch[j][2] == dis_min:
                    dis_catch.append(catch[j])

            up_min = 0xffff
            for w in range(len(dis_catch)):
                if up_min > dis_catch[w][0]:
                    up_min = dis_catch[w][0]

            up_catch = []
            for q in range(len(dis_catch)):
                if dis_catch[q][0] == up_min:
                    up_catch.append(dis_catch[q])

            down_min = 0xffff
            for y in range(len(up_catch)):
                if down_min > up_catch[y][0]:
                    down_min = up_catch[y][0]

            down_catch = []
            for z in range(len(up_catch)):
                if up_catch[z][0] == down_min:
                    down_catch.append(up_catch[z])
            catch = down_catch

        move += catch[0][2]
        eat += 1
        if eat == size:
            size += 1
            eat = 0

        board[current_i][current_j] = 0
        if size >= 7:
            size = 7
        current_i = catch[0][0]
        current_j = catch[0][1]
        board[current_i][current_j] = 9
    else:
        break



print(move)