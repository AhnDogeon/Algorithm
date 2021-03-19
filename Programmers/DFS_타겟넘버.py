# yeonsan = ['+', '-']
# answer = 0
# def solution(numbers, target):
#     def DFS(v, k, total):
#         global answer
#         if v == k:
#             if total + numbers[v] == target:
#                 answer += 1
#             if total - numbers[v] == target:
#                 answer += 1
#             return
#         else:
#             for i in yeonsan:
#                 if i == '+':
#                     total += numbers[v]
#                     DFS(v+1, k, total)
#                     total -= numbers[v]
#                 elif i == '-':
#                     total -= numbers[v]
#                     DFS(v+1, k, total)
#                     total += numbers[v]
#     DFS(0, len(numbers) - 1, 0)
#     return answer

answer = 0
def solution(numbers, target):
    global answer
    DFS(0, numbers, 0, target)
    return answer

def DFS(k, arr, total, target):
    global answer
    if k == len(arr):
        if total == target:
            answer += 1
    else:
        DFS(k + 1, arr, total+arr[k - 1] ,target)
        DFS(k + 1, arr, total-arr[k - 1] ,target)


print(solution([1,1,1,1,1], 3))