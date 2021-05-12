import sys
sys.stdin = open('2960_에라토스테네스의 체.txt', 'r')

N, K = map(int, input().split())

isNumber = [True] * (N + 1)

cnt = 1

for i in range(2, N + 1):
    if isNumber[i] == True:
        for j in range(i, N + 1, i):
            if isNumber[j] == False:
                continue
            if cnt == K:
                print(j)
            isNumber[j] = False
            cnt += 1
