def solution(n, edges):
    answer = 0

    bool_list = [False for _ in range(n)]

    print(bool_list)

    zero_list = []

    for i in range(len(edges)):
        if edges[i][0] == 0:
            zero_list.append(edges[i])


    def DFS(arr):
        print(stack)
        v = stack.pop()
        print(v)
        for j in edges:
            if j[0] == v[1]:
                bool_list[v[1]] = True
        print(bool_list)
    for i in zero_list:
        stack = [i]
        DFS(i)

    return answer


solution(19, [[0,1],[0,2],[0,3],[1,4],[1,5],[2,6],[3,7],[3,8],[3,9],[4,10],[4,11],[5,12],[5,13],[6,14],[6,15],[6,16],[8,17],[8,18]])