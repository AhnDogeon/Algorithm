def solution(N):
    answer = []
    dap = []
    def num_change(n, j):
        result, idx = 0, 0
        while (n >= 1):
            remainder = n % j

            n = n // j

            result += (10 ** idx) * remainder

            idx += 1

        return result

    for i in range(9, 1, -1):
        dap.append(num_change(N, i))


    maxH = 0
    dap_list = []
    for k in dap:
        str_k = str(k)
        tmp = 1
        for m in str_k:
            if m != '0':
                tmp *= int(m)
        dap_list.append(tmp)

    final_idx = dap_list.index(max(dap_list))
    answer.append([9 - final_idx, dap_list[final_idx]])
    print(answer[0])
    return answer
solution(10)