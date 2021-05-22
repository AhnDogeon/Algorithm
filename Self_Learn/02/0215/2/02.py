import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    M_number = list(map(int, input().split())) + [N]
    count = 0
    new_list = []
    original_K = K
    for j in range(N+1):
        if j in M_number:
            new_list.append(j)
        else:
            new_list.append(0)

    for add_number in range(N + 1 - len(M_number)):
        M_number.append(0)

    for i in range(len(new_list) - 1):
        if K == 0:
            if new_list[i]:
                count += 1
                K = original_K
            else:
                count = 0
                break
        else:
            if N - i < K:
                pass
            elif i in M_number:
                if M_number[M_number.index(i) + 1] - M_number[M_number.index(i)] > K:
                    count += 1
                    K = original_K
        K -= 1
    print(f'#{test_case} {count}')