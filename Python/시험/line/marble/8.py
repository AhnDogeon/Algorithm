diff = [(-1, -1),(-1, 0),(-1, 1), (0, -1), (0, 1),(1, -1), (1, 0),(1, 1)]

def solution(board):
    answer = []
    visit = [[[] for _ in range(len(board[0]))] for _ in range(2)]

    print(visit)
    for i in range(2):
        for j in range(len(visit[i])):
            print(board[i][j])
    return answer


solution([".1...2", "111.3."])