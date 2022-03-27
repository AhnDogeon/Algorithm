import sys
sys.stdin = open('17182_우주탐사선.txt', 'r')

N, K = map(int, input().split())

dist = []
for _ in range(N):
    arr = list(map(int, input().split()))
    dist.append(arr)

# 플로이드 워셜
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]


visit = [False for _ in range(N)]
visit[K] = True

answer = 100000000
def DFS(arr, start, depth, time):
    global answer
    if time == N - 1:
        answer = min(answer, depth)
        return
    for i in range(N):
        if arr[i] == False:
            arr[i] = True
            DFS(arr, i, depth + dist[start][i], time + 1)
            arr[i] = False

# cost
DFS(visit, K, 0, 0)

print(answer)