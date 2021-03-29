# version 1 시간초과 꼭 다시 풀어보기
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
        if key <= N and value != 0:
            fail = stages.count(key) / value
            answer.append([key, fail])
        elif key <= N and value == 0:
            fail = 0
            answer.append([key, fail])
            
    answer = sorted(answer, key=lambda x: (-x[1], x[0]))
    final = []
    for f in answer:
        final.append(f[0])
    return final
