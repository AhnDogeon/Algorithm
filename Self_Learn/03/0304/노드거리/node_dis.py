import sys
sys.stdin = open('input.txt', 'r')

def BFS(S, G):
    Dis = [0] * (V + 1)
    Que_list = [S]
    while Que_list:
        v = Que_list.pop(0)
        for j in G[v]:
            if not Dis[j]:
                Dis[j] = Dis[v] + 1
                Que_list.append(j)
    return Dis

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    arr = [[] for _ in range(V + 1)]
    arr[0] = [0]
    for i in range(E):
        node_1, node_2 = map(int, input().split())
        arr[node_1].append(node_2)
        arr[node_2].append(node_1)

    start, end = map(int, input().split())
    result = BFS(start, arr)[end]
    print('#{} {}'.format(test_case, result))