import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    color_red = 1
    color_blue = 2
    count = 0
    for number in range(1, N + 1):
        new_arr = list(map(int, input().split()))
        if new_arr[4] == 1:
            for i in range(new_arr[0], new_arr[2]+1):
                for j in range(new_arr[1], new_arr[3]+1):
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    elif arr[i][j] == 1:
                        pass
                    elif arr[i][j] == 2:
                        count += 1
        elif new_arr[4] == 2:
            for i in range(new_arr[0], new_arr[2]+1):
                for j in range(new_arr[1], new_arr[3]+1):
                    if arr[i][j] == 0:
                        arr[i][j] = 2
                    elif arr[i][j] == 1:
                        count += 1
                    elif arr[i][j] == 2:
                        pass

    print(f'#{test_case} {count}')