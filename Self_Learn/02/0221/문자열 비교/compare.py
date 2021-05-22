import sys
sys.stdin = open('input.txt', 'r')


T = int(input())


for test_case in range(1, T + 1):
    str1 = str(input())
    str2 = str(input())

    i = 0
    j = 0
    count = 0
    while i < len(str2):
        if str2[i] != str1[j]:
            j = 0
            i += 1
        else:
            j += 1
            i += 1
        if j == len(str1):
            count += 1
            break
    print(f'#{test_case} {count}')
