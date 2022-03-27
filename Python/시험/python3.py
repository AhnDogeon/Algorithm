from itertools import combinations


def solution(A):
    # write your code in Python 3.6

    a = list(set(A))
    print(a)

    # 전체 길이가 해답인 경우
    if len(a) == 2:
        return len(A)
    # 조합 구한 후 최대 범위
    comb = list(combinations(a, 2))
    print(comb)

    return


solution([0,5,4,4,5,12])