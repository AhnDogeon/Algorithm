import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1, 11):
    T = int(input())

    board_list = []
    for i in range(100):
        number_list = list(str(input()))
        board_list.append(number_list)

    final_max = 0

    for i in range(100):
        for m in range(2, 101):
            for j in range(100 - m + 1):
                for number in range(int(m / 2)):
                    if board_list[i][j + number] != board_list[i][j + m - 1 - number]:
                        break
                else:
                    if m > final_max:
                        final_max = m

    for j in range(100):
        for m in range(2, 101):
            for i in range(100 - m + 1):
                for number in range(int(m / 2)):
                    if board_list[i + number][j] != board_list[i + m - 1 - number][j]:
                        break
                else:
                    if m > final_max:
                        final_max = m

    print(f'#{test_case} {final_max}')