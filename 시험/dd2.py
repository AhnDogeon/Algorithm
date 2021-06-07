def solution(S):
    minH = "z" * len(S)
    minidx = 1
    for i in range(len(S)):
        result = S[:i] + S[i+1:]
        if result < minH:
            minH = result
            minidx = i
    return minH



print(solution("acb"))