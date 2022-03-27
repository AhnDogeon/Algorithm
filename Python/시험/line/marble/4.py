def solution(k, score):

    # 점수 차가 담긴 리스트
    cha = []
    for i in range(len(score)-1):
        cha.append(score[i] - score[i+1])

    # 점수 차(key)가 k 이상(value)인지 갯수 알려주는 dictionary
    dic = {}
    for j in cha:
        if j in dic.keys():
            dic[j] += 1
        else:
            dic[j] = 1

    # k이상인 점수차를 알려주는 리스트
    lst = []
    for a in dic:
        if dic[a] >= k:
            lst.append(a)

    # k 이상인 점수 차의 인덱스 값을 뽑아내는 리스트
    idx = []
    isIN = True
    while isIN:
        for b in range(len(lst)):
            if lst[b] in cha:
                isIN = True
                idx.append(cha.index(lst[b]))
                k = cha.index(lst[b])
                cha[k] = -1
            else:
                isIN = False


    # idx를 돌면서 score 인덱스를 뽑아내는 set
    ans = set([])
    for d in range(len(idx)):
        ans.add(idx[d])
        ans.add(idx[d]+1)

    result = len(score) - len(ans)
    return result

print(solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]))