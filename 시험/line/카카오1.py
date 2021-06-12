def solution(k, room_number):
    answer = []
    arr_dict = {}
    idx_list = [_ for _ in range(1, k + 1)]
    print(idx_list)
    for i in room_number:
        if arr_dict.get(i):     
            j = idx_list.index(i)
            while True:
                dap = idx_list[j + 1]
                if arr_dict.get(dap):
                    pass
                else:
                    arr_dict[dap] = dap
                    break
                j += 1

        else:
            arr_dict[i] = i
            idx_list.remove(i)
    for j in arr_dict:
        answer.append(arr_dict[j])
    return answer


print(solution(10,[1,3,4,1,3,1]))