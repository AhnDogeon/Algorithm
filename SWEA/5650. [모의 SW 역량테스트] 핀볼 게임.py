T = int(input())

diff = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def DFS(x, y, a, b, start_x, start_y, cnt):
    move = 0
    stack = [[x, y]]
    while stack:
        v = stack.pop()
        dx = v[0] + a
        dy = v[1] + b
        if 0 <= dx < N + 2 and 0 <= dy < N + 2:
            if pan[dx][dy] == 1:
                if a == 0 and b == -1:
                    a = -1
                    b = 0
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == 1 and b == 0:
                    a = 0
                    b = 1
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == 0 and b == 1:
                    a = 0
                    b = -1
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == -1 and b == 0:
                    a = 1
                    b = 0
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
            elif pan[dx][dy] == 2:
                if a == 0 and b == -1:
                    a = 1
                    b = 0
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == 1 and b == 0:
                    a = -1
                    b = 0
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == 0 and b == 1:
                    a = 0
                    b = -1
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == -1 and b == 0:
                    a = 0
                    b = 1
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
            elif pan[dx][dy] == 3:
                if a == 0 and b == -1:
                    a = 0
                    b = 1
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == 1 and b == 0:
                    a = -1
                    b = 0
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == 0 and b == 1:
                    a = 1
                    b = 0
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == -1 and b == 0:
                    a = 0
                    b = -1
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
            elif pan[dx][dy] == 4:
                if a == 0 and b == -1:
                    a = 0
                    b = 1
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == 1 and b == 0:
                    a = 0
                    b = -1
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == 0 and b == 1:
                    a = -1
                    b = 0
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == -1 and b == 0:
                    a = 1
                    b = 0
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
            elif pan[dx][dy] == 5:
                if a == 0 and b == -1:
                    a = 0
                    b = 1
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == 1 and b == 0:
                    a = -1
                    b = 0
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == 0 and b == 1:
                    a = 0
                    b = -1
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
                elif a == -1 and b == 0:
                    a = 1
                    b = 0
                    cnt += 1
                    move += 1
                    stack.append([dx, dy])
            elif pan[dx][dy] == 6 or pan[dx][dy] == 7 or pan[dx][dy] == 8 or pan[dx][dy] == 9 or pan[dx][dy] == 10:
                for worm_idx in worm[pan[dx][dy]]:
                    if worm_idx != [dx, dy]:
                        dx = worm_idx[0]
                        dy = worm_idx[1]
                        move += 1
                        stack.append([dx, dy])
                        break
            elif [dx, dy] in black:
                return cnt
            elif dx == start_x and dy == start_y and move >= 1:
                return cnt
            elif pan[dx][dy] == 0:
                move += 1
                stack.append([dx, dy])





for test_case in range(1, T + 1):
    N = int(input())
    pan = []
    pan.append([5] * (N + 2))
    for i in range(N):
        pan.append([5] + list(map(int, input().split())) + [5])
    pan.append([5] * (N + 2))
    black = []
    worm = [[], [], [], [], [], [], [], [], [], [], []]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if pan[i][j] == 6 or pan[i][j] == 7 or pan[i][j] == 8 or pan[i][j] == 9 or pan[i][j] == 10:
                worm[pan[i][j]].append([i, j])
            elif pan[i][j] == -1:
                black.append([i, j])
    max_cnt = 0
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if pan[x][y] == 0:
                for (a, b) in diff:
                    cnt = 0
                    start_x = x
                    start_y = y
                    z = DFS(x, y, a, b, start_x, start_y, cnt)
                    if max_cnt < z:
                        max_cnt = z
    print('#{} {}'.format(test_case, max_cnt))