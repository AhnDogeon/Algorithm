from copy import deepcopy
cnt = 0
result = []
def solution(A,B,C,D):
    input_list = [A, B, C, D]
    visit = [False, False, False, False]
    arr = []
    def DFS(arr, R, input_list):
        global cnt
        if R == 4:
            if arr not in result:
                deeparr = deepcopy(arr)
                result.append(deeparr)
                cnt += 1
        else:
            if R == 0:
                for i in range(len(input_list)):
                    if visit[i] == False and input_list[i]<=2:
                        arr.append(input_list[i])
                        visit[i] = True
                        DFS(arr,R+1, input_list)
                        arr.pop()
                        visit[i] = False
            elif R == 1:
                for j in range(len(input_list)):
                    if arr[0] == 2:
                        if visit[j] == False and input_list[j] < 5:
                            arr.append(input_list[j])
                            visit[j] = True
                            DFS(arr, R + 1, input_list)
                            arr.pop()
                            visit[j] = False
                    else:
                        if visit[j] == False:
                            arr.append(input_list[j])
                            visit[j] = True
                            DFS(arr, R + 1, input_list)
                            arr.pop()
                            visit[j] = False
            elif R == 2:
                for k in range(len(input_list)):
                    if visit[k] == False and input_list[k]<=5:
                        arr.append(input_list[k])
                        visit[k] = True
                        DFS(arr,R+1, input_list)
                        arr.pop()
                        visit[k] = False

            elif R == 3:
                for m in range(len(input_list)):
                    if visit[m] == False:
                        arr.append(input_list[m])
                        visit[m] = True
                        DFS(arr,R+1, input_list)
                        arr.pop()
                        visit[m] = False
    R = 0
    DFS(arr, R, input_list)
    return cnt
print(solution(6,2,4,7))