import sys
sys.stdin = open('17136_색종이 붙이기.txt', 'r')


board = [list(map(int, input().split())) for _ in range(10)]

one_cnt = 0
for _ in range(10):
    for __ in range(10):
        if board[_][__] == 1:
            one_cnt += 1

paper_list = [5, 5, 5, 5, 5] # 0 : 5x5 1 : 4x4 2: 3X3 3: 2x2 4: 1x1
def check(i, j, size):
    for check_x in range(5-size):
        for check_y in range(5-size):
            if 0 <= i+check_x < 10 and 0 <= j+check_y < 10:
                if board[i+check_x][j+check_y] == 0:
                    return False
            else:
                return False
    return True


def paper(depth):
    global answer, one_cnt
    if answer > 0 and depth >= answer:
        return
    if one_cnt == 0:
        if answer > depth or answer == -1:
            answer = depth
        return

    isFind = False
    for x in range(10):
        for y in range(10):
            if board[x][y] == 1:
                isFind = True
                break
        if isFind:
            break

    before_list = []
    if board[x][y] and isFind == True:
        for v in range(len(paper_list)):
            if paper_list[v] >= 1:
                if check(x, y, v):
                    put_total = 0
                    for put_x in range(5-v):
                        for put_y in range(5-v):
                            board[x+put_x][y+put_y] = 0
                            before_list.append([x+put_x, y+put_y])
                            put_total += 1
                    one_cnt -= put_total
                    paper_list[v] -= 1
                    paper(depth+1)
                    one_cnt += put_total
                    paper_list[v] += 1

                    for back in before_list:
                        board[back[0]][back[1]] = 1


answer = -1
paper(0)
print(answer)