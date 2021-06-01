import sys
sys.stdin = open('4828_minmax.txt')


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(max(arr) - min(arr))