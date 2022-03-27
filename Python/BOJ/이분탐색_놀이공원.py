############# Version 1###################
# N, M = map(int, input().split())
# t = list(map(int, input().split()))
#
# l = 1
# r = 10**20
# max_m = max_s = 0
#
# while l <= r:
#     mid = (l+r)//2
#     s = sum((mid-1)//x + 1 for x in t)
#     if s < N:
#         if max_m < mid:
#             max_m = mid
#             max_s = s
#         l = mid + 1
#     else:
#         r = mid - 1
#
# for i, k in enumerate(t):
#     if max_m % k == 0:
#         max_s += 1
#         if max_s == N:
#             print(i+1)
#             break

########### Version 2 ############
if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    t_list = list(map(int, sys.stdin.readline().split()))

    if n < m:
        print(n)
    else:
        # 이분 탐색
        left, right = 0, 60000000000
        t = None
        while left <= right:
            mid = (left + right) // 2
            cnt = m
            for i in range(m):
                cnt += mid // t_list[i]
            if cnt >= n:  # n명을 태울 수 있는 상황
                t = mid
                right = mid - 1
            else:
                left = mid + 1

        # t - 1에 탑승한 아이들의 숫자를 계산한다.
        cnt = m
        for i in range(m):
            cnt += (t - 1) // t_list[i]

        # t에 탑승한 아이를 계산한다.
        for i in range(m):
            if t % t_list[i] == 0:  # t 시간에 탑승한 아이
                cnt += 1
            if cnt == n:
                print(i + 1)
                break