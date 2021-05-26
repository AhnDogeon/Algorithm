import sys
sys.stdin = open('1.txt', 'r')

def Go(x, y, board):
    one_time = False
    while True:
        if x == len(board):
            return True
        elif board[x][y] == '#':
            x += 1
        elif board[x][y] == '>':
            y += 1
        elif board[x][y] == '<':
            y -= 1
        elif board[x][y] == '*':
            if one_time == False:
                x += 1
                one_time = True
            elif one_time == True:
                return False


def solution(drum):
    answer = 0
    for i in range(len(drum[0])):
        start_x = 0
        start_y = i
        result = Go(start_x, start_y, drum)
        if result == True:
            answer += 1

    return answer

arr = []
for _ in range(1000):
    k = str(input())
    arr.append(k)
print(solution(arr))
