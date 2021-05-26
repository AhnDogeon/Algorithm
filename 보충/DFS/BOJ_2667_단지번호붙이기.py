import sys
sys.stdin = open('BOJ_2667_단지번호붙이기.txt', 'r')

N = int(input())

board = []
visit_board = []
for _ in range(N):
    board.append(list(str(input())))
    visit_board.append([False]*N)

diff = [(0, -1),(1, 0),(0, 1),(-1, 0)]
def DFS(i, j, final_result):
    global board, visit_board, result
    visit_board[i][j] = True
    board[i][j] = '0'
    for (a, b) in diff:
        di, dj = i + a, j + b
        if 0 <= di < N and 0 <= dj < N:
            if visit_board[di][dj] == False and board[di][dj] == '1':
                visit_board[di][dj] = True
                board[di][dj] = '0'
                result += 1
                DFS(di, dj, final_result)
    # print(result)
    final_result.append(result)

count = 0
final = []
for x in range(N):
    for y in range(N):
        if board[x][y] == '1':
            final_result = []
            result = 1
            DFS(x, y, final_result)
            count += 1
            final.append(max(final_result))
        result = 1

print(count)
final.sort()
if final:
    for _ in range(len(final)):
        print(final[_])
else:
    print(0)