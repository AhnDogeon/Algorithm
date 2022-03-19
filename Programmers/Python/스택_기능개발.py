# def solution(progresses, speeds):
#     answer = []
#     arr = []
#     for i in range(len(progresses)):
#         cnt = 100 - progresses[i]
#         if (cnt % speeds[i]):
#             arr.append(int(cnt / speeds[i] + 1))
#         else:
#             arr.append(int(cnt / speeds[i]))
#
#
#     dap = 0
#     while (arr):
#         start = arr[0]
#         idx = 0
#         for j in range(len(arr)):
#             if arr[j] > start:
#                 answer.append(dap)
#                 dap = 0
#                 break
#             else:
#                 idx += 1
#                 dap += 1
#         for k in range(idx):
#             arr.pop(0)
#         if not arr:
#             answer.append(dap)
#
#     return answer

# version 2
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))