answer = 0


def solution(user_id, banned_id):
    global answer

    def DFS(x, arr):
        global answer
        for j in arr:
            for idx in range(len(x)):
                if j[idx] == '*':
                    pass
                else:
                    if j[idx] == x[idx]:
                        pass
                    else:
                        answer += 1
                        arr.pop(idx)
                        for k in arr:
                            DFS(k, arr)
                        arr.insert(idx)
                        break

    for i in user_id:
        DFS(i, banned_id)

    return answer

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"])