def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)


    for i in new_lost:
        if i + 1 in new_reserve:
            new_reserve.remove(i+1)
        elif i - 1 in new_reserve:
            new_reserve.remove(i - 1)
        else:
            n -= 1


    return n


print(solution(7, [1,3,5], [3,4,7]))