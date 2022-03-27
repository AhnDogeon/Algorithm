# import sys
# sys.stdin = open('7675_통역사 성경이.txt', 'r')

# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = str(input())
#     # result = arr.split(".")

#     end_list = ['.', '?', '!']

#     sentence = []
#     result = ''
#     for i in arr:
#         if i not in end_list:
#             result += i
#         else:
#             result += i
#             sentence.append(result)
#             result = ''

#     print('#{}'.format(test_case), end=' ')
#     number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     for j in sentence:
#         cnt = 0
#         final = ''
#         for k in j:
#             if k == ' ' or k in end_list:
#                 up = 0
#                 low = 0
#                 number = 0
#                 for m in final:
#                     if m.isupper():
#                         up += 1
#                     elif m in number_list:
#                         number += 1
#                 else:
#                     if up == 1 and number == 0:
#                         cnt += 1
#                 final = ''

#             else:
#                 final += k
#         print(cnt, end=' ')
#     else:
#         print()
tmp = 0
R = 10
def DFS(v):
    global tmp
    if v == R:
        print(tmp)
        return
    else:
        tmp += v
        DFS(v+1)

DFS(0)