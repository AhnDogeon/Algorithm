import sys
sys.stdin = open('input.txt', 'r')

def BFS(start, G):
    visited = [False] * (N + 1)
    Dis = [0] * (N + 1)
    Q=[start]
    visited[start] = True
    while Q:
        v = Q.pop(0)
        for i in G[v]:
            if not visited[i]:
                Dis[i] = Dis[v] + 1
                visited[i] = True
                Q.append(i)
    return Dis


for test_case in range(1, 11):
    N, start = map(int, input().split())
    arr = []
    arr.extend(list(map(int, input().split())))

    G = [[] for _ in range(N + 1)]

    for i in range(0, len(arr), 2):
        G[arr[i]].append(arr[i+1])


    result = BFS(start, G)

    maxH = result[0]
    count = 0
    for x in result:
        if x >= maxH:
            maxH = x
            final_count = count
        count += 1
    print('#{} {}'.format(test_case, final_count))