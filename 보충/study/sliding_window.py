

def sliding_window(arr, k):
    start = 0

    for end in range(len(arr)):
        copy_arr = arr[start:end + 1]
        print(copy_arr)
        if end >= k - 1:
            start += 1
    return

if __name__ == '__main__':
    A = [1,2,3,4,4,5]
    for i in range(2, len(A) + 1):
        sliding_window(A, i)