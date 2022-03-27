def solution(h, w, n, board):
    answer = 0
    print(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                visit = [[[True] * w] * h]

    return answer


solution(7,9,4,["111100000","000010011","111100011","111110011","111100011","111100010","111100000"])
