def solution(rows, columns, swipes):
    board = []
    cnt = 1
    for i in range(rows):
        sub = []
        for j in range(columns):
            sub.append(cnt)
            cnt += 1
        board.append(sub)

    for arr in swipes:
        d = arr[0]
        total = 0

        sub = []
        for x in range(arr[1] - 1, arr[3]):
            for y in range(arr[2] - 1, arr[4]):
                sub.append([x, y, board[x][y]])

        if d == 1:
            # start
            sub_sub = []
            for i in range(arr[2], arr[4] + 1):
                total += board[-1][i - 1]
                sub_sub.append(board[-1][i - 1])

            for k in sub:
                if k[2] not in sub_sub:
                    board[k[0]+1][k[1]] = k[2]
                else:
                    board[0][k[1]] = k[2]
            print(board)
        elif d == 2:
            sub_sub = []
            for i in range(arr[2], arr[4] + 1):
                total += board[-1][i - 1]
                sub_sub.append(board[0][i - 1])

            for k in sub:
                if k[2] not in sub_sub:
                    board[k[0] + 1][k[1]] = k[2]
                else:
                    board[0][k[1]] = k[2]
            print(board)

        elif d == 3:
            sub_sub = []
            for i in range(arr[2], arr[4] + 1):
                total += board[-1][i - 1]
                sub_sub.append(board[-1][i - 1])

            for k in sub:
                if k[2] not in sub_sub:
                    board[k[0] + 1][k[1]] = k[2]
                else:
                    board[0][k[1]] = k[2]
            print(board)

        elif d == 4:
            sub_sub = []
            for i in range(arr[2], arr[4] + 1):
                total += board[-1][i - 1]
                sub_sub.append(board[-1][i - 1])

            for k in sub:
                if k[2] not in sub_sub:
                    board[k[0] + 1][k[1]] = k[2]
                else:
                    board[0][k[1]] = k[2]
            print(board)
    return board

solution(4, 3,[[1,1,2,4,3],[3,2,1,2,3],[4,1,1,4,3],[2,2,1,3,3]])