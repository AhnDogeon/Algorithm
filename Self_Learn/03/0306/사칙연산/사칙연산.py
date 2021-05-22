import sys
sys.stdin = open('사칙연산.txt', 'r')

def inorder(n):
    if n == 0:
        return
    if G[n] == '+':
        return inorder(L[n]) + inorder(R[n])
    elif G[n] == '-':
        return inorder(L[n]) - inorder(R[n])
    elif G[n] == '*':
        return inorder(L[n]) * inorder(R[n])
    elif G[n] == '/':
        return inorder(L[n]) // inorder(R[n])
    else:
        return G[n]


for test_case in range(1, 11):
    N = int(input())
    L = [0 for _ in range(N + 1)]
    R = [0 for _ in range(N + 1)]
    P = [0 for _ in range(N + 1)]
    G = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        arr = list(map(str, input().split()))
        if len(arr) == 4:
            for j in range(1, len(arr)):
                if j == 1:
                    G[i] = arr[j]
                elif j == 2:
                    L[i] = int(arr[j])
                    P[int(arr[j])] = i
                elif j == 3:
                    R[i] = int(arr[j])
                    P[int(arr[j])] = i
        else:
            for j in range(1, len(arr)):
                if j == 1:
                    G[i] = int(arr[j])

    print('#{} {}'.format(test_case, inorder(1)))