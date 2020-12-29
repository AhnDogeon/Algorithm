def solution(clothes):
    clothes_dict = {}
    for info in clothes:
        if info[1] in clothes_dict:
            clothes_dict[info[1]].append(info[0])
        else:
            clothes_dict[info[1]] = [info[0]]
    
    answer = 1
    for i in clothes_dict.values():
        answer *= len(i) + 1
    answer -= 1
    return answer