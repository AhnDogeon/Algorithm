from copy import deepcopy
def solution(tickets):
    answer = []
    visit = [False for _ in range(len(tickets))]
    def DFS(start, arr, visit):
        for i in range(len(tickets)):
            if tickets[i][0] == start and visit[i] == False:
                visit[i] = True
                arr.append(tickets[i][1])
                DFS(tickets[i][1], arr, visit)
                arr.pop()
                visit[i] = False
        if visit.count(True) == len(visit):
            tmp = deepcopy(arr)
            answer.append(tmp)
    DFS("ICN", ["ICN"], visit)

    while True:
        result = deepcopy(answer)
        isDap = False
        whenbreak = answer[0][1]
        for k in range(1, len(answer[0])):
            for j in range(len(answer)):
                if answer[j][k] != whenbreak:
                    dap = sorted(answer, key=lambda x : x[j])
                    isDap = True
                    break
            if isDap == True:
                break
        answer = dap[:j+1]
        if len(answer) == 1:
            break

    return answer[0]

print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]))