import sys
sys.stdin = open('17135_캐슬디펜스.txt', 'r')




diff = [(-1,0),(1,0),(0, -1),(0, 1)]

board = []

for _ in range(6):
    input_list = list(map(int, input().split()))
    board.append(input_list)
print(board)

visit = [[False, False,False,False,False],[False, False,False,False,False],[False, False,False,False,False],[False, False,False,False,False],[False, False,False,False,False],[False, False,False,False,False]]
def DFS(x, y):
    visit[x][y] = True
    arr = []
    for (a, b) in diff:
        dx, dy = x + a, y+ b
        if visit[dx][dy] == False and 0<=dx <6 and 0<= dy < 5:
            DFS(dx, dy)


DFS(4,1)