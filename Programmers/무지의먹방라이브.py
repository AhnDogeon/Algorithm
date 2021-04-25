def solution(food_times, k):
    answer = -1
    food_dict = {}
    for idx, value in enumerate(food_times):
        food_dict[idx+1] = value
    time = 0
    start = 1
    print(food_dict)

    key_list = list(food_dict.keys())
    while time < k and key_list:
        for i in food_dict.keys():
            if start == i:
                food_dict[i] -= 1
                if food_dict[i] == 0:
                    del food_dict[i]
                    idx = key_list.index(i)
                    key_list.remove(i)
                    if idx > len(key_list) - 1:
                        idx -= len(key_list)
                    try:
                        start = key_list[idx]
                    except:
                        break
                else:
                    a = (key_list.index(i) + 1) % len(key_list)
                    start = key_list[a]
                break

    print(start)
solution([3,1,2], 5)