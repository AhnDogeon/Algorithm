import sys
sys.stdin = open('17471_게리맨더링(DFS).txt', 'r')

maxH = 0xffff
N = int(input())

people = list(map(int, input().split()))

arr = []

for _ in range(N):
    v = list(map(int, input().split()))
    arr.append(v[1:])

def DFS(x, dfs_list):
    # [[2, 4], [1, 3, 6, 5], [4, 2], [1, 3], [2], [2]]
    visit[x-1] = True
    for w in arr[x - 1]:
        if visit[w-1] == False and w in dfs_list:
            DFS(w, dfs_list)

def check():
    if visit.count(True) == N:
        return True
    else:
        return False

def hap(arr_one, arr_two):
    total_one = 0
    for one in arr_one:
        total_one += people[one - 1]

    total_two = 0
    for two in arr_two:
        total_two += people[two - 1]

    return abs(total_one - total_two)

def johap(k, s):
    global visit, maxH
    if k == R:
        visit = [False] * N
        other_list = []
        for j in range(len(number_list)):
            if number_list[j] not in result:
                other_list.append(number_list[j])
        total = hap(result, other_list)
        if total < maxH:
            DFS(result[0], result)
            DFS(other_list[0], other_list)
            ch = check()
            # 모든걸 다 돌았을 때 total 초기화
            if ch == True:
                maxH = total
    else:
        for i in range(s, N + k - R + 1):
            result[k] = number_list[i]
            johap(k+1, i+1)


number_list = [_ for _ in range(1, N+1)]
DFS_list = []
for R in range(1, N//2+1):
    result = [0] * R
    johap(0,0)
if maxH == 0xffff:
    maxH = -1

print(maxH)