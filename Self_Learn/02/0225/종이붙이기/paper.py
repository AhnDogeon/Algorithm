import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for test_case in range(1, T+1):
    number = int(input())


    def paper(N):
        if N == 10:
            return 1
        elif N == 20:
            return 3
        elif ((N / 10) % 2) == 0:
            return 2 * paper(N-10) + 1
        else:
            return 2 * paper(N-10) - 1

    print(f'#{test_case}', end=' ')
    print(paper(number))
