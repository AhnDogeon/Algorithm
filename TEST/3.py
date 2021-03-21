def solution(enter, leave):
    answer = [0 for _ in range(len(enter))]


    for idx in range(len(enter)):
        # idx 는 내 위치
        # 나보다 먼저 들어온
        for i in enter[:idx]:
            a = leave.index(i)
            b = leave.index(enter[idx])
            if (a >= b):
                answer[enter[idx] - 1] += 1
                answer[a] += 1
        # 나보다 나중에 들어온
        for j in enter[idx+1:]:
            a = leave.index(j)
            b = leave.index(enter[idx])
            if (a <= b):
                answer[enter[idx] - 1] += 1
                answer[a] += 1
    print(answer)
    for k in range(len(answer)):
        if answer[k] != 0:
            answer[k] -= 1
    return answer

solution([3,2,1], [2,1,3])