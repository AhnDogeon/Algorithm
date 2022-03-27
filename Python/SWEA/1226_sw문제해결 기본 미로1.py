import sys
sys.stdin = open('1226_sw문제해결 기본 미로1.txt', 'r')


T = 10
for test_case in range(1, T + 1):
    test_number = int(input())
    board = []
    for _ in range(16):
        input_list = []
        input_list.extend(list(input()))
        board.append(input_list)
    #
    # print('================디버깅====================')
    # for i in range(16):
    #     for j in range(16):
    #         print(board[i][j], end=' ')
    #     print()
    # print('================디버깅====================')

    start = [1, 1]
    end = [13, 13]

    visit = []
    for i in range(16):
        visit_line = []
        for j in range(16):
            if board[i][j] == '1':
                visit_line.append(True)
            elif board[i][j] == '0' or board[i][j] == '2' or board[i][j] == '3':
                visit_line.append(False)
        visit.append(visit_line)

    # print(visit)
    #
    # print('================디버깅====================')
    # for i in range(16):
    #     for j in range(16):
    #         print(visit[i][j], end=' ')
    #     print()
    # print('================디버깅====================')
    #

    result = 0

    diff = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    def DFS(x, y):
        global result
        visit[x][y] = True
        if [x, y] == end:
            result = 1
            return
        else:
            for (a, b) in diff:
                dx, dy = x + a, y + b
                if 0 <= dx < 16 and 0 <= dy < 16 and visit[dx][dy] == False:
                    DFS(dx, dy)

    DFS(start[0], start[1])
    print('#{} {}'.format(test_number, result))