def DFS(x):
    visit[x] = True
    result.append(x)
    for i in board[x]:
        if visit[i] != True:
            DFS(i)

N = int(input())

board = [[] for _ in range(N + 1)]
visit = [ False for _ in range(N + 1)]

node = int(input())
for i in range(node):
    m1, m2 = map(int, input().split())
    board[m1].append(m2)
    board[m2].append(m1)
result= []
DFS(1)
print(len(result)-1)