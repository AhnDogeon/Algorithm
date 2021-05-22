import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    str1 = list(str(input()))
    str2 = list(str(input()))

    max_count = 0
    for i in str1:
        count = 0
        for j in str2:
            if i == j:
                count += 1
        else:
            if count > max_count:
                max_count = count


    print(f'#{test_case} {max_count}')