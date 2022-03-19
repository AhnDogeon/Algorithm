def solution(genres, plays):
    answer = []

    album = {}

    idx = 0
    for g, p in zip(genres, plays):
        try:
            album[g].append([idx, p])
        except:
            album[g] = [[idx, p]]
        idx += 1

    sum_album = {}
    for item, value in album.items():
        total = 0
        for i in value:
            total += i[1]
        sum_album[item] = total

    sum_list = sorted(sum_album.items(), key=lambda x: x[1], reverse=True)

    for item, value in album.items():
        album[item] = sorted(value, key=lambda x: (x[1], -x[0]), reverse=True)

    for sum_arr in sum_list:
        answer.append(album[sum_arr[0]][0][0])
        try:
            answer.append(album[sum_arr[0]][1][0])
        except:
            continue
    return answer