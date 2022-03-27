import sys
sys.stdin = open('이진힙.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr=[0]
    arr.extend(list(map(int, input().split())))
    G = [0 for _ in range(N + 1)]

    for i in range(N + 1):
        G[i] = arr[i]
        root = i//2
        while root >= 1:
            if G[i] < G[root]:
                G[i], G[root] = G[root], G[i]
            root = root//2
            i = i//2

    result = 0
    i = len(G) - 1
    while i >= 1:
        i = i // 2
        result += G[i]
    print('#{} {}'.format(test_case,result))