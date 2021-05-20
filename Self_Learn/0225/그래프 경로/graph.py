import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V + 1)]
    visit = [False for _ in range(V + 1)]
    for i in range(E):
        u, v = map(int, input().split())
        node[u].append(v)
    start, end = map(int, input().split())
    
    def DFS(v):
        stack = []
        stack.append(v)
        result = []
        visit[v] = True
        result += [v]

        while len(stack) > 0:
            prev = v
            for w in node[v]:
                if not visit[w]:
                    stack.append(w)
                    v = w
                    visit[w] = True
                    result += [v]
                    break
            if prev == v:
                v = stack.pop()
        if end in result:
            print(1)
        else:
            print(0)
    print(f'#{test_case}',end=" ")
    DFS(start)




