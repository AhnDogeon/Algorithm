def solution(n, times):
    answer = 0
    leng = len(times)
    left = 1
    right = n * max(times)

    while left <= right:
        mid = (left + right) // 2
        total = 0

        for time in times:
            total += mid // time

            if total > n:
                break

        if total < n:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    return answer