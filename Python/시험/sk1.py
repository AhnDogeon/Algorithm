# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
answer = False


def DFS(t, DFS_dict, total):
    global answer
    next = t + 1
    if t == total:
        answer = True
        return
    if next in DFS_dict[t]:
        DFS(next, DFS_dict, total)
    else:
        return


def solution(N, A, B):
    # write your code in Python 3.6
    global answer
    totalA = max(A)
    totalB = max(B)
    total = max(totalA, totalB)
    pass_dict = {}
    for i in range(len(A)):
        try:
            pass_dict[A[i]].append(B[i])
        except:
            pass_dict[A[i]] = [B[i]]
        try:
            pass_dict[B[i]].append(A[i])
        except:
            pass_dict[B[i]] = [A[i]]

    DFS(1, pass_dict, total)
    return answer

print(solution(6, [2,4,5,3], [3,5,6,4]))