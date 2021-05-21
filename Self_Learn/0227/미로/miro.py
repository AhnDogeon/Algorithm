import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 미로의 범위
    board = []

    for miro in range(N + 2):
        if miro == 0 or miro == N + 1:
            one_line = []
            for one in range(N + 2):
                one_line.append('1')
            board.append(one_line)
        else:
            line = list(input())
            line.insert(0, '1')
            line.append('1')
            board.append(line)

    # board : 미로
    def start(x, y): # 스택에 쌓기
        stack.append([x, y])


    stack = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '2':
                start(i, j)
                a = i
                b = j
            elif board[i][j] == '3':
                end = [i, j]

    result = 0
    while len(stack) != 0:
        if [a + 1, b] == end or [a - 1, b] == end or [a, b + 1] == end or [a, b - 1] == end:
            result = 1
            break
        if board[a - 1][b] == '0': # 위
            a -= 1
            start(a, b)
            board[a][b] = '1'

        elif board[a][b + 1] == '0': # 오른
            b += 1
            start(a, b)
            board[a][b] = '1'

        elif board[a + 1][b] == '0': # 아래
            a += 1
            start(a, b)
            board[a][b] = '1'

        elif board[a][b - 1] == '0': # 왼
            b -= 1
            start(a, b)
            board[a][b] = '1'

        # 3을 찾았을 때!
        else:
            del stack[-1]
            if len(stack) != 0:
                a = stack[-1][0]
                b = stack[-1][1]
            else:
                break


    print(f'#{test_case} {result}')