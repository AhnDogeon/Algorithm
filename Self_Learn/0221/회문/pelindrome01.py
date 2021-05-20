import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    board_list = []
    for i in range(N):
        number_list = list(str(input()))
        board_list.append(number_list)
    # 가로
    for i in range(N):
        for j in range(N - M + 1):
            for number in range(int(M / 2)):
                if board_list[i][j + number] != board_list[i][j + M - 1 - number]:
                    break
            else:
                print(f'#{test_case} ', end='')
                for result in range(M):
                    print(f'{board_list[i][j+result]}', end='')
                print()

    # 세로
    for j in range(N):
        for i in range(N - M + 1):
            for number in range(int(M / 2)):
                if board_list[i+number][j] != board_list[i + M - 1 - number][j]:
                    break
            else:
                print(f'#{test_case} ', end='')
                for result in range(M):
                    print(f'{board_list[i+result][j]}', end='')
                print()
