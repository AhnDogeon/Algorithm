import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    number = int(input())
    max_count = 0
    for i in str(number):
        count = 0
        for j in str(number):
            if j == i:
                count += 1
            if count > max_count:
                max_count = count
                result = i


    print(f'#{test_case} {result} {max_count}')