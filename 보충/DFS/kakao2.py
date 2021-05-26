def solution(orders, course):
    answer = []
    orders = sorted(orders)
    arr = []
    MaxH = max(orders, key=len)
    for i in orders:
        for j in i:
            if j not in arr:
                arr.append(j)
    N = len(arr)
    result_dict = {}
    def comb_r(k, s, R):  # 조합
        if k == R:
            cnt = 0
            tt = ''.join(sorted(t))
            for i in orders:
                ii = ''.join(sorted(i))
                if tt in ii:
                    cnt += 1
            if R in result_dict:
                if cnt < result_dict[R][1]:
                    return

            result = ''.join(t)
            if R in result_dict:
                if result_dict[R][1] == cnt:
                    result_dict[R][0].append(result)
                elif result_dict[R][1] < cnt:
                    result_dict[R][0] = [result]
                    result_dict[R][1] = cnt
                else:
                    return
            else:
                result_dict[R] = [[result], cnt]
        else:
            for i in range(s, N + (k - R) + 1):
                t[k] = arr[i]
                comb_r(k + 1, i + 1, R)
    for R in course:
        if R <= len(MaxH):
            t = [0] * R
            comb_r(0, 0, R)

    for d in result_dict:
        if result_dict[d][1] >= 2:
            for e in result_dict[d][0]:
                e = sorted(e)
                dap = ''.join(e)
                answer.append(dap)
    answer.sort()
    return answer


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))