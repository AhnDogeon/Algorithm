import sys
sys.stdin = open('input.txt', 'r')


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12]
T = int(input())
for test_case in range(1, T + 1):
    count = 0
    N, K = map(int, input().split())
    for i in range(1<< len(A)):
        bubun_list = []
        for j in range(len(A)):
            if i & (1<<j):
                bubun_list.append(A[j])
        total = 0
        for hap in bubun_list:
            total += hap
        if total == K and len(bubun_list) == N:
            count += 1


    print(f'#{test_case} {count}')


