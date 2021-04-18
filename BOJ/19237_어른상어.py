import sys
sys.stdin = open('19237_어른상어.txt', 'r')

N, M, k = map(int, input().split())

board = []
smell_board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    arr = [0 for _ in range(N)]
    smell_board.append(arr)

current_direc = list(map(int, input().split()))
current_pos = [[] for _ in range(M)]

print(current_pos)
for i in range(N):
    for j in range(N):
        if board[i][j]:
            current_pos[board[i][j] - 1] = [i, j]


shark_direc = {}
for s in range(M):
    shark_direc[s] = []
    for _ in range(4):
        shark_direc[s].append(list(map(int, input().split())))

time = 0
cnt = M
# board 상어의 위치 판
# smell_board 상어의 냄새 판
# current_direc 상어의 방향 리스트
def Smell():
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                smell_board[i][j] = k

direc = [(-1, 0),(1, 0),(0, -1),(0, 1)]
def Move():
    pos_cnt = -1
    for [x, y] in current_pos:
        pos_cnt += 1
        print(x, y)
        iDirec = current_direc[pos_cnt]
        direc_arr = shark_direc[pos_cnt][iDirec-1]
        print(direc_arr)
        for next_direc in direc_arr:
            dx = direc[iDirec-1][0]
            dy = direc[iDirec-1][1]
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < N and 0<= next_y < N:
                if not smell_board[next_x][next_y]:




def MinusSmell():
    for i in range(N):
        for j in range(N):
            if smell_board[i][j]:
                smell_board[i][j] -= 1

def Count():
    shark_count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                shark_count += 1
    return shark_count

while(cnt > 1):
    Smell()
    time += 1
    Move()
    MinusSmell()
    cnt = Count()
    if cnt == 1:
        break
