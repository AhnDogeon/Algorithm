import sys
sys.stdin = open('15686_치킨배달.txt', 'r')


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

chicken_house = []
for _ in range(N):
    for __ in range(N):
        if board[_][__] == 2:
            chicken_house.append([_, __])

house = []
for x in range(N):
    for y in range(N):
        if board[x][y] == 1:
            house.append([x, y])

chicken_com = [___ for ___ in range(M)]
t = [0] * M

result = []
def com(k, s):
    if k == M:
        before_result = []
        for j in house:
            maxH = 0xffff
            for chicken in t:
                total = abs(j[0] - chicken[0]) + abs(j[1] - chicken[1])
                if total < maxH:
                    maxH = total
            before_result.append(maxH)
        result.append(sum(before_result))
    else:
        for i in range(s, len(chicken_house) + (k - M) + 1):
            t[k] = chicken_house[i]
            com(k+1, i+1)
com(0, 0)

print(min(result))