def solution(s):
    answer = []
    arr = []
    for i in range(1, len(s)-1):
        if s[i] == '{':
            start = i
        if s[i] == '}':
            end = i
            arr.append(s[start+1:end])
    tmp = 1
    print(arr)
    arr.sort(key=len)
    for j in arr:
        index_list = j.split(',')
        for k in index_list:
            if int(k) not in answer:
                answer.append(int(k))
    return answer

solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")