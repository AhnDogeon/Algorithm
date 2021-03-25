def solution(board, moves):
    answer = 0
    stack = []
    # i는 인덱스
    for i in moves:
        for j in range(len(board)):
            if (board[j][i - 1]):
                stack.append(board[j][i - 1])
            if len(stack) >= 2:
                if stack[-1] == stack[-2]:
                    stack.pop(-1)
                    stack.pop(-2)
                    answer += 2
        print(stack)
    print(answer)
    
    return answer