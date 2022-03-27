import sys
from itertools import combinations

sys.stdin = open('17142_연구소3.txt', 'r')

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


diff = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def BFS(virus):
    global zero_cnt, M, N
    time = 1
    cnt = 0
    num = M
    fake_zero = zero_cnt
    if fake_zero == 0:
        return 0
    else:
        while virus:
            num -= 1
            v = virus.pop(0)
            for (l, s) in diff:
                dx, dy = v[0] + l,  v[1] + s
                if 0 <= dx < N and 0 <= dy < N:
                    if copy_board[dx][dy] == 0:
                        copy_board[dx][dy] = 2
                        fake_zero -= 1
                        cnt += 1

                        virus.append([dx, dy])

                    elif copy_board[dx][dy] == -1:
                        copy_board[dx][dy] = 2
                        cnt += 1

                        virus.append([dx, dy])
            if num == 0:
                if fake_zero == 0:
                    return time
                else:
                    time += 1
                    num = cnt
                    cnt = 0
        return -1



#  바이러스 개수 세기

virus = []
virus_cnt = 0
zero_cnt = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j])
            virus_cnt += 1
        elif board[i][j] == 0:
            zero_cnt += 1


no = list(combinations(virus, virus_cnt - M))



final = []
for x in range(len(no)):
    copy_board = [[0] * N for _ in range(N)]

    for a in range(N):
        for b in range(N):
            if board[a][b] != 0:
                copy_board[a][b] = board[a][b]

    for y in range(len(no[x])):
        copy_board[no[x][y][0]][no[x][y][1]] = -1
        for [c, d] in virus:
            if [c, d] == [no[x][y][0], no[x][y][1]]:
                virus.remove([c,d])
    # print('==================================')
    # for co in range(N):
    #     for py in range(N):
    #         print(copy_board[co][py], end=' ')
    #     print()
    # print('==================================')

    result = BFS(virus)
    if result != -1:
        final.append(result)

    virus = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                virus.append([i, j])


if len(final) == 0:
    print(-1)
else:
    print(min(final))