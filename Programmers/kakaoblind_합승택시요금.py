def solution(n, s, a, b, fares):
    answer = 10000000
    maxH = 10000000
    # 노드 갯수 n
    # 출발지점 s, 도착지점 a, b
    dist = [[maxH] * n for i in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for arr in fares:
        x = arr[0] - 1
        y = arr[1] - 1
        cost = arr[2]
        dist[x][y] = cost
        dist[y][x] = cost

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for t in range(n):  # 경유점에 따라 최소 합승 비용 탐색
        temp = dist[s - 1][t] + dist[t][b - 1] + dist[t][a - 1]
        answer = min(answer, temp)

    return answer