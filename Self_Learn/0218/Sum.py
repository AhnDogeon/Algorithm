import sys
sys.stdin = open("input.txt", "r")


for test_case in range(1, 11):
    N = int(input())
    arr = []
    for number in range(1,101):
        arr.append(list(map(int, input().split())))

    hang_total = 0

    for i in range(0, 100):
        hang_result = 0
        for j in range(0, 100):
            hang_result += arr[i][j]
            if hang_result > hang_total:
                hang_total = hang_result

    yul_total = 0

    for i in range(0, 100):
        yul_result = 0
        for j in range(0, 100):
            yul_result += arr[j][i]
            if yul_result > yul_total:
                yul_total = yul_result

    same_total = 0
    same_result = 0
    for i in range(0, 100):
        for j in range(0, 100):
            if i == j:
                same_result += arr[i][j]
            if same_result > same_total:
                same_total = same_result

    reverse_total = 0
    reverse_result = 0
    for i in range(0, 100):
        for j in range(99, -1, -1):
            if (i + j) == 100:
                reverse_result += arr[i][j]
            if reverse_result > reverse_total:
                reverse_total = reverse_result

    final_result = max(same_total, yul_total, hang_total, reverse_total)
    print(f'#{test_case} {final_result}')