import sys

sys.stdin = open('1644_소수의 연속합.txt', 'r')

n = int(input())

num = [True] * (n + 1)
num[0] = num[1] = False
for i in range(2, n + 1):
    if num[i]:
        t = 2
        while i * t <= n:
            num[i * t] = 0
            t += 1

prime = sorted([i for i in range(2, n + 1) if num[i]], reverse=True)
len_prime = len(prime)
ans = 0

if len_prime >= 1:
    lo, hi, tmp = 0, 1, prime[0]
    while lo < len_prime:
        if tmp >= n:
            if tmp == n:
                ans += 1
            tmp -= prime[lo]
            lo += 1
        # tmp < n
        elif hi == len_prime:
            break
        else:
            tmp += prime[hi]
            hi += 1

print(ans)