def solutions(rooms, target):
    answer = []
    room_dict = {}
    for i in rooms:
        number = i[1:i.index(']')]
        if number in room_dict:
            room_dict[number].append(i[i.index(']'):])
        else:
            room_dict[number] = i[i.index(']') + 1:].split(',')
    people = []
    for room in room_dict:
        people.extend(room_dict[room])
        if int(room) != target:
            answer.append([room_dict[room], abs(target - int(room))])
    answer = sorted(answer, key = lambda x:x[1])
    final = []
    forfinaltwo = []
    for i in answer:
        forfinalone = []
        for j in i[0]:
            if people.count(j) > 1:
                forfinaltwo.append([j, people.count(j)])
            else:
                forfinalone.append(j)

        forfinalone.sort()
        final.extend(forfinalone)

    forfinaltwo = sorted(forfinaltwo, key=lambda x: x[1])
    for k in forfinaltwo:
        if k[0] not in final:
            final.append(k[0])
    for i in final:
        if i in room_dict[str(target)]:
            final.remove(i)
    print(final)
    return final


solutions(["[1234]None,Of,People,Here","[5678]Wow"], 1234)