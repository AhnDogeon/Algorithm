import sys
sys.stdin = open('21610_마법사 상어와 비바라기.txt', 'r')

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


diff = [[0, 0], [0, -1], [-1, -1],[-1, 0],[-1, 1],[0, 1],[1, 1],[1, 0],[1, -1]]

def Move(dir, dis):
    # dir 방향, dis 거리
    for _ in range(len(cloud)):
        x = cloud.pop(0)
        dx, dy = x[0] + (diff[dir][0] * dis), x[1] + (diff[dir][1] * dis)
        while dx < 0:
            dx = N + dx
        while dx >= N:
            dx = dx - N
        while dy < 0:
            dy = N + dy
        while dy >= N:
            dy = dy - N

        cloud.append([dx, dy])

def Copy(cloud):
    # diff의 2, 4, 6, 8번만 확인
    copy_diff = [2, 4, 6, 8]
    for i in cloud:
        cnt = 0
        for j in copy_diff:
            dx, dy = i[0] + diff[j][0], i[1] + diff[j][1]
            if 0 <= dx < N and 0 <= dy < N:
                if board[dx][dy]:
                    cnt += 1
        board[i[0]][i[1]] += cnt

def Make_cloud(cloud):
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and [i, j] not in cloud:
                board[i][j] -= 2
                new_cloud.append([i, j])

    return new_cloud


cloud = [[N - 1, 0],[N - 1, 1],[N -2 , 0],[N - 2, 1]] # 구름 시작 위치
for _ in range(M):
    d, s = map(int, input().split())
    #1번 조건
    Move(d, s)
    # 2번 조건
    for i in cloud:
        board[i[0]][i[1]] += 1
    #3번 조건 not
    #4번 조건 대각선 물복사
    Copy(cloud)
    cloud = Make_cloud(cloud)

total = 0
for i in range(N):
    for j in range(N):
        total += board[i][j]
print(total)