def solution(info, query):
    answer = []

    info_list = []
    for i in info:
        info_list.append(i.split(' '))
    print(info_list)
    arr  = []
    for i in info_list:
        arr.append(i[:-1])
    print(arr)
    dup = {}
    for x, y in enumerate(arr):
        dup[x] = y
    print(dup)

    for j in query:
        result = 0
        j = j.replace(' ', '')
        list = j.split('and')
        a = list.pop()
        if 'pizza' in a:
            list.append('pizza')
            #b = a.replace('pizza', '')
            #list.append(b)
        elif 'chicken' in a:
            list.append('chicken')
            #b = a.replace('chicken', '')
            #list.append(b)
        else:
            list.append('-')
            b = a.replace('-', '')
            #list.append('-')
            #list.append(b)
        print(list)
        # print(list)
        # x가 시험자, list가 query
        # for x in info_list:
        #     if int(x[4]) < int(list[4]):
        #         continue
        #     if list[3] != '-':
        #         if x[3] != list[3]:
        #             continue
        #     if list[2] != '-':
        #         if x[2] != list[2]:
        #             continue
        #     if list[1] != '-':
        #         if x[1] != list[1]:
        #             continue
        #     if list[0] != '-':
        #         if x[0] != list[0]:
        #             continue
        #     result += 1
        # answer.append(result)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))