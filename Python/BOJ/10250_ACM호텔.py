T = int(input())

for test_case in range(1, T + 1):
    H, W, N = map(int, input().split()) # 층수, 방수, 몇 번째 손님
    board = []
    for _ in range(H):
        board.append([False] * W)

    count = 0
    for i in range(W):
        for j in range(H):
            if board[j][i] == False:
                board[j][i] = True
                count += 1
                if count == N:
                    if i+1 >= 10:
                        print('{}{}'.format(j + 1, i + 1))
                    else:
                        print('{}{}{}'.format(j+1, 0, i+1))