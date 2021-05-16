import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    pizza = [1 for _ in range(N)]

    count = 0
    pizza_index = [0 for _ in range(N)]
    index_number = 1
    while count != N - 1:
        for i in range(N):
            if pizza[i] == 1:
                if len(arr) == 0:
                    pizza[i] = pizza[i] // 2
                    pass
                else:
                    pizza_index[i] = index_number
                    index_number += 1
                    pizza[i] = (arr[0])
                    del arr[0]
            else:
                pizza[i] = pizza[i] // 2

            count = 0
            for j in pizza:
                if j == 0:
                    count += 1
            if count == N - 1:
                break

    for result in range(len(pizza)):
        if pizza[result] != 0:
            print(f'#{test_case} {pizza_index[result]}')
