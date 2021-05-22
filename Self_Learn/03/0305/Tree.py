import sys
sys.stdin = open('input.txt', 'r')

def inorder(n):
    if n == 0:
        return
    inorder(L[n])
    print(word_list[n], end='')
    inorder(R[n])



for test_case in range(1, 11):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    word_list = [False] * (N + 1)
    for number in range(N):
        arr = list(map(str, input().split()))
        for input_length in range(len(arr)):
            index_number = int(arr[0])
            if input_length == 1:
                word_list[index_number] = arr[1]
            elif input_length == 2:
                L[index_number] = int(arr[2])
            elif input_length == 3:
                R[index_number] = int(arr[3])
    print('#{}'.format(test_case), end=' ')
    inorder(1)
    print()