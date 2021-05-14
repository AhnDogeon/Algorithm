import sys
sys.stdin = open('3321_최고의피자(그리디).txt', 'r')

N = int(input())

A, B = map(int, input().split())

C = int(input())

kal = []
for _ in range(N):
    kal.append(int(input()))

print(kal)

total = 0
# 피자 총 가격 분모
# 총 칼로리 분자


def johap(k, n, bits):
    if k == n:
        for i in range(len(bits)):
            if bits[i]:

            else:
                pass
        return
    bits[k] = 0
    johap(k+1, n, bits)
    bits[k] = 1
    johap(k+1, n, bits)


arr = [0] * len(kal)
johap(0, len(kal), arr)