import sys
sys.stdin = open('엔터프라이즈4.txt', 'r')

N, M = map(int, input().split())

arr_dict = {}
arr_list = []
for _ in range(M):
    s1, s2, cost = map(str, input().split())
    arr_list.append([s1, s2, cost])
    if s1 in arr_dict.keys():
        arr_dict[s1].append([s2, cost])
    else:
        arr_dict[s1] = [[s2, cost]]

print(arr_dict)
question = int(input())

for _ in range(question):
    q1, q2 = map(str, input().split())
    answer = [0xffff]
    def DFS(x, y, result):
        if x == y:
            answer.append(result)
            return
        if result >= min(answer):
            return
        for i in arr_dict: # i는 key 값
            if i == x:
                for j in arr_dict[i]:
                    DFS(j[0], y, int(j[1])+result)
    for k in arr_list:
        if k[0] == q1:
            DFS(q1, q2, 0)
    if min(answer) != 0xffff:
        print(min(answer))
    elif q1 == q2:
        print(0)
    else:
        print(-1)