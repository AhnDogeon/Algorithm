import sys
import copy
sys.stdin = open('input.txt', 'r')


T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(str, input()))

    while len(arr) >= 2:
        arr_copy = copy.deepcopy(arr)
        for i in range(len(arr_copy)-1):
            if arr_copy[i] == arr_copy[i+1]:
                same = i
                break
        else:
            break
        del arr[same:same+2]
        arr_copy = copy.deepcopy(arr)

    print(f'#{test_case} {len(arr)}')