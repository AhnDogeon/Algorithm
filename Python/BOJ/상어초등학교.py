from copy import deepcopy

N = int(input())

number_arr = []
number_dict = {}

# 번호별 테이블 세팅
# 입력 순서 배열 생성
for i in range(N * N):
    input_arr = list(map(int, input().split()))
    number = input_arr[0]
    number_arr.append(number)
    number_dict[number] = number_dict.get(number, []) + input_arr[1:]

# 채워넣을 빈 테이블 생성
board = []
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(-1)
    board.append(temp)

# 인접한 곳에 몇 개 있는지 확인하는 함수
diff = [(0, -1),(0, 1),(1, 0),(-1, 0)]
def Run(target):
    copy_board = deepcopy(board)
    max_cnt = 0
    idx_arr = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == -1:
                cnt = 0
                next_cnt = 0
                for dx, dy in diff:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] == -1:
                            next_cnt += 1
                        if board[nx][ny] in number_dict[target]:
                            cnt += 1
                if cnt > max_cnt:
                    idx_arr = [[x, y, next_cnt, cnt]]
                    max_cnt = cnt
                elif cnt == max_cnt:
                    max_cnt = cnt
                    idx_arr.append([x, y, next_cnt, cnt])
    
    idx_arr.sort(key=lambda x : (-x[3],-x[2], x[0], x[1]))
    return idx_arr[0]


for key in number_arr:
    input_arr = Run(key)
    input_x, input_y = input_arr[0], input_arr[1]
    board[input_x][input_y] = key


# 마지막 만족도 계산
total = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for x, y in diff:
            dx, dy = x+ i, y + j
            if 0<= dx < N and 0 <= dy < N:
                if board[dx][dy] in number_dict[board[i][j]]:
                    cnt += 1
        if cnt == 0:
            total += 0
        elif cnt == 1:
            total += 1
        elif cnt == 2:
            total += 10
        elif cnt == 3:
            total += 100
        elif cnt == 4:
            total += 1000

print(total)
