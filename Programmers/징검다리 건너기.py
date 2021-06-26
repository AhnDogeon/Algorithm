from copy import deepcopy


def Check(zero, arr):
    string_arr = str(arr)
    string_zero = str(zero)
    string_zero = string_zero[1:-1]
    if string_zero in string_arr:
        return True
    else:
        return False


def solution(stones, k):
    answer = 0
    zero_list = [0] * k
    right = 0xfffff
    left = 1
    M = int((right + left) / 2)

    while True:
        copy_stones = deepcopy(stones)
        for i in range(len(stones)):
            copy_stones[i] -= M
            if copy_stones[i] < 0:
                copy_stones[i] = 0

        bResult = Check(zero_list, copy_stones)
        # 더 이상 건널 수 없는 경우
        # M이 더 작아져야함 left쪽으로
        if bResult:
            right = M
            M = int((right + left) / 2)
        # 아직 더 건널 수 있는 경우
        # M이 더 커져야함 right쪽으로
        else:
            left = M
            M = int(right + left / 2)
        if left == M or right == M or (left + 1 == M and right - 1 == M):
            break

    return M

print(solution([2,4,5,3,2,1,4,2,5,1],3))