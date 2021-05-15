import sys
sys.stdin = open('subtree.txt', 'r')

T = int(input())

def inorder(n):
    if n == 0:
        return
    global count
    count += 1
    inorder(L[n])
    inorder(R[n])

for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)
    for i in range(0, len(arr), 2):
        u, v = arr[i], arr[i+1]
        if L[u] == 0:
            L[u] = v
        elif R[u] == 0:
            R[u] = v
        P[v] = u
    count = 0
    inorder(N)

    print('#{} {}'.format(test_case, count))