import sys
from copy import deepcopy
sys.stdin = open('3190_뱀.txt', 'r')

N = int(input())

K = int(input())

time = 0

apple = []
for _ in range(K):
    x, y = map(int, input().split())
    apple.append([x, y])

L = int(input())

direc = []
for _ in range(L):
    t, dir = map(str, input().split())
    t = int(t)
    direc.append([t, dir])
snake = [[1, 1]]
time = 0
dir_change = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 0 - 상
# 1 - 하
# 2 - 좌
# 3 - 우
current_dir = 3
True_break = False
while True:
    while_cnt = len(snake)
    copy_snake = deepcopy(snake)
    v = snake.pop(0)
    dx, dy = v[0] + dir_change[current_dir][0], v[1] + dir_change[current_dir][1]
    if dx == 0 or dx == N + 1 or dy == 0 or dy == N + 1 or [dx, dy] in snake:
        time += 1
        True_break = True
        break
    if [dx, dy] in apple: # 열매가 있는 자리 일 경우
        snake = []
        snake.insert(0, [dx, dy])
        for snake_x in copy_snake:
            snake.append(snake_x)
        apple.pop(apple.index([dx, dy]))

    else:
        snake = []
        snake.insert(0, [dx, dy])
        copy_snake.pop()
        for snake_x in copy_snake:
            snake.append(snake_x)
    time += 1
    if True_break == True:
        break
    for d in direc:
        if d[0] == time: # 방향 바꾸는 경우
            if current_dir == 0:
                if d[1] == 'D':
                    current_dir = 3
                elif d[1] == 'L':
                    current_dir = 2
            elif current_dir == 1:
                if d[1] == 'D':
                    current_dir = 2
                elif d[1] == 'L':
                    current_dir = 3
            elif current_dir == 2:
                if d[1] == 'D':
                    current_dir = 0
                elif d[1] == 'L':
                    current_dir = 1
            elif current_dir == 3:
                if d[1] == 'D':
                    current_dir = 1
                elif d[1] == 'L':
                    current_dir = 0
            direc.pop(direc.index(d))
            break

print(time)
