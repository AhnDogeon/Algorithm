def solution(m, k):
    answer = ''

    arr = []
    for i in range(len(k)):
        arr.append(k[i])

    index_list = []

    copy_m = m
    start = 0
    while (arr):
        first_word = arr.pop(0)
        for k in range(start, len(m)):
            if m[k] == first_word:
                start = k + 1
                break
            else:
                answer += m[k]


    if start < len(m):
        answer += m[start:]
    print(answer)

    return answer

solution('kkkkkk', 'abk')