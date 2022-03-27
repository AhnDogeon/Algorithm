from itertools import combinations
import copy

def findtwo(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 2:
                DFS(i, j, arr)


def DFS(a, b, arr):
    global N
    global M
    D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in D:
        x= a + i[0]
        y = b + i[1]
        if 0 <= x < N and 0 <= y < M:
            if arr[x][y] == 0:
                arr[x][y] = 2
                DFS(x, y, arr)


N, M = map(int, input().split())

arr = []
for line in range(N):
    arr.append(list(map(int, input().split())))

zero_list = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 0:
            zero_list.append([i,j])

one_list = list(combinations(zero_list, 3))

count_list = []
for x in one_list:
    trash = copy.deepcopy(arr)
    for y in x:
        trash[y[0]][y[1]] = 1
    findtwo(trash)

    count = 0
    for a in trash:
        tmp = a.count(0)
        count += tmp
    count_list.append(count)
result = max(count_list)

print(result)