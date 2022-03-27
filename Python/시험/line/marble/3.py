def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    t = 0
    Que = [begin]
    arr = []
    while t < len(target):
        v = Que.pop(0)
        for i in range(len(v)):
            tmp = v[i]
            v = v.replace(v[i], target[i])
            if v in words:
                arr.append(v)
            v = v.replace(v[i], tmp)
        if target in arr:
            answer = t
            break
        t += 1
        Que = arr

    return answer

solution('hit',	'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])