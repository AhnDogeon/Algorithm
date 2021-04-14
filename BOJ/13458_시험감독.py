import sys
sys.stdin = open('13458_시험감독.txt', 'r')

N = int(input())

Ai = list(map(int, input().split()))

B, C = map(int, input().split())

cnt = N

for i in range(len(Ai)):
    Ai[i] -= B

for j in range(len(Ai)):
    if Ai[j] >= 0:
        z = Ai[j] / C
        if Ai[j] % C:
            cnt = cnt + int(Ai[j] / C) + 1
        else:
            cnt = cnt + (int(Ai[j] / C))

print(cnt)