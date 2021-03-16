def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)):
        cnt = 100 - progresses[i]
        if (cnt % speeds[i]):
            arr.append(int(cnt / speeds[i] + 1))
        else:
            arr.append(int(cnt / speeds[i]))


    dap = 0
    while (arr):
        start = arr[0]
        idx = 0
        for j in range(len(arr)):
            if arr[j] > start:
                answer.append(dap)
                dap = 0
                break
            else:
                idx += 1
                dap += 1
        for k in range(idx):
            arr.pop(0)
        if not arr:
            answer.append(dap)

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))