def solution(S, C):
    # write your code in Python 3.6
    email = '@' + C.lower() + '.com'
    name_dict = {}
    S_list = S.split('; ')


    count_name = []
    for i in S_list:
        result = ''
        name_list = i.split(' ')
        # 성과 이름만 주어질 경우
        if len(name_list) == 2:
            first = name_list[0].lower()
            Last = name_list[1].lower()
            result = Last + '_' + first
            if result not in count_name:
                count_name.append(result)
                name_dict[i] = result
            else:
                cnt = count_name.count(result) + 1
                name_dict[i] = result + str(cnt)
                count_name.append(result)
        # 미들네임 주어질 경우
        elif len(name_list) > 2:
            first = name_list[0].lower()
            Last = name_list[2].lower()
            if ('-' in Last):
                Last = Last.replace('-', '')
            result = Last + '_' + first
            if result not in count_name:
                count_name.append(result)
                name_dict[i] = result
            else:
                cnt = count_name.count(result) + 1
                name_dict[i] = result + str(cnt)
                count_name.append(result)

    final = ''

    for i, key in enumerate(name_dict):
        if (i == len(name_dict) - 1):
            answer = key + ' ' + '<' + name_dict[key] + email + '>'
        else:
            answer = key + ' ' + '<' + name_dict[key] + email + '>; '
        final += answer
    print(final)
    return final

solution('John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker', 'Example')