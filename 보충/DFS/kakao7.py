from itertools import product


def solution(sales, links):
    answer = 0xffff
    link_dict = {}
    for x, y in links:
        if x in link_dict:
            link_dict[x].append(y)
        else:
            link_dict[x] = [y]
    for i in link_dict:
        link_dict[i].append(i)
    my_list = []
    for j in link_dict.values():
        my_list.append(j)
    a = list(product(*my_list))
    items = list(set([tuple(set(item)) for item in a]))
    for arr in items:
        result = 0
        print(arr)
        if (sum(sales[x-1] for x in arr) >= answer):
            continue
        for dap in set(arr):
            result += sales[dap-1]
            if result >= answer:
                break
        if result < answer:
            answer = result
    return answer


print(solution([14,17,15,18,19,14,13,16,28,17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))