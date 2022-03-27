# N = int(input())

# arr = list(map(int, input().split()))
arr = [120, 110, 140, 150]
# budget = int(int(input()))
N = 4
budget = 485
left = 0
right = max(arr)

total = 0
# 1번 조건`
if sum(arr) <= budget:
    print(max(arr))
else:
    while (left <= right):
        mid = (left + right) // 2
        total = 0
        for i in arr:
            if i <= mid:
                total += i
            else:
                total += mid
        if total > budget:
            right = mid - 1
        else:
            result = mid
            left = mid + 1
    print(result)