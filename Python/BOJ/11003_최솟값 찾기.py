import sys
sys.stdin = open('11003_최솟값 찾기.txt', 'r')

N, T = map(int, input().split())

arr = list(map(int, input().split()))

def sliding_window(arr, k):
    start = 0
    window_sum = 0xfffff

    for end in range(len(arr)):
        copy_arr = arr[start:end + 1]

        minH = min(copy_arr)
        print(minH, end=' ')

        if end >= (k - 1):
            start += 1

    return window_sum


sliding_window(arr, T)