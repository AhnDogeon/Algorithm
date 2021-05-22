import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    maxH = 0
    minH = arr[0]
    for j in range(1, N+1):
        for i in arr:
            if i > maxH:
                maxH = i
            if i < minH:
                minH = i
        arr[arr.index(maxH)] = maxH-1
        maxH-=1
        
        arr[arr.index(minH)] = minH+1
        minH+=1
    for i in arr:
        if i > maxH:
            maxH = i
        if i < minH:
            minH = i
        
    print(f'#{test_case} {maxH - minH}')