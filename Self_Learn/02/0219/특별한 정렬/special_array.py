import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    new_list=[]
    for i in range(1,6):
        maxH = 0
        minH = arr[0]
        for j in arr:
            if j >= maxH:
                maxH = j
            if j <= minH:
                minH = j
        new_list.append(maxH)
        new_list.append(minH)
        del arr[arr.index(maxH)]
        del arr[arr.index(minH)]

    print(f'#{test_case}', end=' ')
    for result in new_list:
        print(f'{result}', end=' ')
    print()