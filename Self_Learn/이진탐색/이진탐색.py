import sys
sys.stdin = open('이진탐색.txt', 'r')

def inorder(v):
    global arr
    if v == 0:
        return
    # 전위 자리
    inorder(L[v])
    arr.append(v)
    inorder(R[v])


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    L = [0 for _ in range(N + 1)]
    R = [0 for _ in range(N + 1)]

    root = 1
    while root * 2 <= N:
        L[root] = root * 2
        root += 1

    root = 1
    while root * 2 + 1 <= N:
        R[root] = root * 2 + 1
        root += 1
    inorder(1)
    result_root = arr.index(1) + 1
    result_N2 = arr.index(N//2) + 1

    print('#{} {} {}'.format(test_case, result_root, result_N2))