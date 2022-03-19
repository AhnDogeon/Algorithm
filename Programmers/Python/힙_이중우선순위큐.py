def solution(operations):
    Que = []
    for op in operations:
        num = op.split(" ")
        if num[0] == 'I':
            Que.append(int(num[1]))
        elif num[0] == 'D':
            if num[1] == '1':
                try:
                    Que.remove(max(Que))
                except:
                    continue
            elif num[1] == '-1':
                try:
                    Que.remove(min(Que))
                except:
                    continue
    if len(Que) == 0:
        return [0, 0]
    else:
        return [max(Que), min(Que)]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))