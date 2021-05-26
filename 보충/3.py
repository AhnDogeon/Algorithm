def solution(data):
    answer = []
    time = 0
    v = data.pop(0)
    answer.append(v[0])
    time = v[1] + v[2]
    ans = 0
    while ans <= len(data):
        wait = []
        for dap in data:
            if dap[1] <= time:
                wait.append(dap)
        wait = sorted(wait, key=lambda x: x[2])
        if len(wait) > 0:
            v = wait.pop(0)
            data.remove(v)
            answer.append(v[0])
            time += v[2]
        ans += 1
    answer.append(data[0][0])
    return answer

print(solution([[1, 0, 5],[2, 2, 2],[3, 3, 1],[4, 4, 1],[5, 10, 2]]))