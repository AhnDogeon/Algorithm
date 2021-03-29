def solution(N, stages):
    answer = []
    start = 1
    
    stage_dict = {}
    for i in range(N + 1):
        stage_dict[i + 1] = 0
    
    for x in stages:
        for y in range(x):
            stage_dict[y+1] += 1
    
    for key, value in stage_dict.items():
        if key <= N:
            fail = stages.count(key) / value
            answer.append([key, fail])
            
    answer = sorted(answer, key=lambda x: (-x[1], x[0]))
    final = []
    for f in answer:
        final.append(f[0])
    return final