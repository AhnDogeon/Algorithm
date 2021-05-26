def solution(new_id):
    arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.']

    new_id = new_id.lower()
    answer = ''
    # 2번 조건
    for i in new_id:
        if i.islower():
            answer += i
        else:
            if i in arr:
                answer += i
    dap = ''
    dot = ''
    for j in answer:
        if j == '.':
            dot += '.'
        else:
            if dot == '':
                dap += j
            else:
                dap += '.'
                dap += j
                dot = ''
    answer = dap.strip('.')
    if answer == '':
        answer += 'a'
    if len(answer) >= 16:
        answer = answer[0:15]

    result = answer.strip('.')

    while (len(result)<=2):
        result += result[-1]
    return result


print(solution('안도건안ㄷ관아ㅓㄹ엄랴ㅓㅁ댜ㅐㅈ러ㅣㅁㅇ라널'))