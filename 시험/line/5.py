import sys

sys.stdin = open('5.txt', 'r')
diff = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def BFS(s,e):
    lst = [[s, e]]
    v = lst[0]
    visit = [[False for _ in range(y+1)] for _ in range(x+1)]
    visit[v[0]][v[1]] = True
    while lst:
        v = lst.pop(0)
        for (a, b) in diff:
            dx, dy = v[0] + a, v[1] + b
            if 0 <= dx < x + 1 and 0 <= dy < y + 1 and visit[dx][dy] == False:
                visit[dx][dy] = True
                dis[dx][dy] = dis[v[0]][v[1]] + 1
                lst.append([dx, dy])


n, m = map(int, input().split())
y, x = map(int, input().split())
if y < 0 or y >= n or x < 0 or x >= m:
    print('Fail')
else:
    pan = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dis = [[0 for _ in range(y+1)] for _ in range(x+1)]


    BFS(0,0)
    print(dis[-1][-1])

    for c in range(len(pan)):
        for d in range(len(pan[c])):
            if c == 0:
                pan[c][d] = 1
            elif d == 0:
                pan[c][d] = 1
            else:
                pan[c][d] = pan[c-1][d] + pan[c][d-1]
    print(pan[-1][-1])