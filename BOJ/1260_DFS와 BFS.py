import sys
sys.stdin = open('1260_DFS와 BFS.txt', 'r')

N, M, V = map(int, input().split6())

# N 정점의 개수
# M 간선의 개수
# V 시작할 정점의 번호

arr = [[] for _ in range(M + 1)]

for m in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
print(arr)
def DFS(v):
    DFS_stack = []


def BFS(v):
    visit_BFS = [False] * (N + 1)
    Dis = [0] * (N + 1)
    Que = [v]
    while Que:
        v = Que.pop(0)
        print(v)
        for j in sorted(arr[v]):
            if not visit_BFS[j]:
                Dis[j] = Dis[v] + 1
                visit_BFS[j] = True
                Que.append(j)
    # return Dis

# DFS(V)
BFS(V)