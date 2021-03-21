def solution(inp_str):
    answer = []
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['~', '!', '@', '#', '$', '%', '^', '&', '*']
    # 1번 규칙
    if len(inp_str) < 8 or len(inp_str) > 15:
        answer.append(1)
    # 2번 규칙
    isTrue = [False, False, False, False]
    for i in inp_str:
        if (i.encode().isalpha()):
            if i.isupper():
                isTrue[0] = True
            elif i.islower():
                isTrue[1] = True
            pass
        elif i in number:
            isTrue[2] = True
            pass
        elif i in special:
            isTrue[3] = True
            pass
        else:
            if 2 not in answer:
                answer.append(2)
            if isTrue.count(True) >= 3:
                break
            else:
                continue


    # 3번 규칙 만들기
    ###
    if isTrue.count(True) < 3:
        answer.append(3)


    start = inp_str[0]
    # 4번 규칙
    cnt = 0
    for j in inp_str:
        if cnt == 4:
            answer.append(4)
            break
        if j == start:
            cnt += 1
        else:
            cnt = 1
            start = j

    number_dict = {}
    for k in inp_str:
        if k in number_dict.keys():
            number_dict[k] += 1
            if number_dict[k] == 5:
                answer.append(5)
                break
        else:
            number_dict[k] = 1

    if len(answer) == 0:
        answer.append(0)

    answer.sort()
    return answer

print(solution("AaTa+!12-3"))