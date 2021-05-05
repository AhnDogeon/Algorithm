from itertools import permutations
from copy import deepcopy


def solution(expression):
    answer = 0

    per = ['*', '+', '-']
    per = list(permutations(per))

    arr = []
    board = ''
    for i in expression:
        try:
            int(i)
            board += i
        except:
            arr.append(int(board))
            arr.append(i)
            board = ''
    else:
        arr.append(int(board))

    for i in range(len(arr)):
        arr[i] = str(arr[i])

    for yeonsan in per:
        copy_arr = deepcopy(arr)
        yeonsan = list(yeonsan)
        while yeonsan:
            yeon = yeonsan.pop(0)
            while yeon in copy_arr:
                idx = copy_arr.index(yeon)
                y = ''.join(copy_arr[idx - 1:idx + 2])
                x = [str(eval(y))]
                copy_arr = copy_arr[:idx - 1] + x + copy_arr[idx + 2:]
        if abs(int(copy_arr[0])) >= answer:
            answer = abs(int(copy_arr[0]))

    return answer