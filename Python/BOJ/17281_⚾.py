def bestSet(n, s):
    import itertools
    from functools import reduce
    if n > s:
        return [-1]
    a = list(itertools.combinations_with_replacement(range(s + 1), n))
    print(a)
    combinations = [i for i in itertools.combinations_with_replacement(range(s+1), n) if sum(i) == s]

    multiply_li = [reduce(lambda x,y: x*y, combination) for combination in combinations]
    index = multiply_li.index(max(multiply_li))
    return sorted(list(combinations[index]))


bestSet(3,5)