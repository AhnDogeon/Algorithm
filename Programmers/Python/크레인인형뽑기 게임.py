def solution(board, moves):
    answer = 0
    stack = []
    # i는 인덱스
    for i in moves:
        print(i)
        for a in range(len(board)):
            for b in range(len(board[a])):
                print(board[a][b], end=' ')
            print()
        print(stack)
        print('-----------------------------------------------')
        for j in range(len(board)):
            if (board[j][i - 1]):
                stack.append(board[j][i - 1])
                board[j][i - 1] = 0
                if len(stack) >= 2:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2
                break


    return answer


solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
         [1, 5, 3, 5, 1, 2, 1, 4])