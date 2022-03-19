def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    total1 = 0
    total2 = 0
    total3 = 0
    for num in range(len(answers)):
        if answers[num] == supo1[num % len(supo1)]:
            total1 += 1
        if answers[num] == supo2[num % len(supo2)]:
            total2 += 1
        if answers[num] == supo3[num % len(supo3)]:
            total3 += 1
    answer.append(total1)
    answer.append(total2)
    answer.append(total3)
    print(answer)

    result = []
    if answer.count(max(answer)) >= 2:
        for i in range(len(answer)):
            if answer[i] == max(answer):
                result.append(i + 1)
    else:
        result.append(answer.index(max(answer)) + 1)

    return result