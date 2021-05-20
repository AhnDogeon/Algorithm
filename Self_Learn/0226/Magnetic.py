import sys
sys.stdin = open("input.txt", "r")


for test_case in range(1, 11):
    rectangle = int(input())
    board = []
    for line in range(rectangle):
        board.append(list(map(int, input().split())))

    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for x in range(i + 1, len(board)):
                    if board[x][j] == 1:
                        board[x][j] = 0
                        pass
                    elif board[x][j] == 2:
                        count += 1
                        break

    print(f'#{test_case} {count}')