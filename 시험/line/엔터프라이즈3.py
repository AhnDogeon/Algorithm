import sys
sys.stdin = open('엔터프라이즈3.txt', 'r')

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(float(input()))

result = round(sum(arr) / M, 2)

cnt = 0
arr_2 = []

for i in arr:
    cnt += i // result
    arr_2.append(i % result)

while cnt <= M:
    if int(cnt) == M:
        break
    result -= 0.005
    cnt = 0
    for i in arr:
        cnt += i // result

result = round(result, 2)

print("{0:.2f}".format(result))