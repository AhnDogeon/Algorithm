# # version 1 시간초과 꼭 다시 풀어보기
# def solution(N, stages):
#     answer = []
#     start = 1
    
#     stage_dict = {}
#     for i in range(N + 1):
#         stage_dict[i + 1] = 0

#     for x in stages:
#         for y in range(x):
#             stage_dict[y+1] += 1

#     for key, value in stage_dict.items():
#         if key <= N and value != 0:
#             fail = stages.count(key) / value
#             answer.append([key, fail])
#         elif key <= N and value == 0:
#             fail = 0
#             answer.append([key, fail])
            
#     answer = sorted(answer, key=lambda x: (-x[1], x[0]))
#     final = []
#     for f in answer:
#         final.append(f[0])
#     return final

def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N+1):
        count = stages.count(i)
        # 실패율 = 도달하지못한인원/스테이지에 도달한 수
        # 스테이지에 도달한 유저가 없는 경우 
        if count == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        # length에서 도달하지 못한 인원은 뺀다
        length -= count
    
    # 실패율 기준으로 내림차순
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer