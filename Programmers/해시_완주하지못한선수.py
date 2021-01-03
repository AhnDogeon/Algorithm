def solution(participant, completion):
    participant_dict = {}
    answer = ''
    for i in participant:
        if i in participant_dict:
            participant_dict[i] += 1
        else:
            participant_dict[i] = 1

    for j in completion:
        participant_dict[j] -= 1

    k = sorted(participant_dict.items(), key=lambda x: x[1], reverse = True)
    answer = k[0][0]
    return answer