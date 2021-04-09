N, M = map(int, input().split())
t = list(map(int, input().split()))

l = 1
r = 10**20
max_m = max_s = 0

while l <= r:
    mid = (l+r)//2
    s = sum((mid-1)//x + 1 for x in t)
    if s < N:
        if max_m < mid:
            max_m = mid
            max_s = s
        l = mid + 1
    else:
        r = mid - 1

for i, k in enumerate(t):
    if max_m % k == 0:
        max_s += 1
        if max_s == N:
            print(i+1)
            break