def solution(n, edge):
    answer = 0

    isGo = [False for _ in range(n)]
    distance = [0 for _ in range(n)]

    node_dict = {}
    for m, n in edge:
        try:
            node_dict[m].append(n)
        except:
            node_dict[m] = [n]
        try:
            node_dict[n].append(m)
        except:
            node_dict[n] = [m]
    print(node_dict)

    def BFS(n, k):
        distance[n - 1] = k
        Que = node_dict[n]
        isGo[n - 1] = True
        while Que:
            v= Que.pop(0)
            isGo[v - 1] = True
            for i in node_dict[v]:
                if isGo[i - 1] == False:
                    isGo[i - 1] = True
                    Que.append(i)
                    distance[i - 1] = distance[v - 1] + 1
        print(distance)


    BFS(1, 0)

    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])