import sys
sys.stdin = open('노드의합.txt', 'r')

def list_number(v):
    global G
    G[(v - 1) // 2] = G[v] + G[v - 1]



T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())

    G = [0 for _ in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        G[u] = v

    if len(G) % 2:
        G.append(0)

    for i in range(len(G) - 1, 1, -2):
        # 11 9 7 5 3
        list_number(i)

    print('#{} {}'.format(test_case, G[L]))