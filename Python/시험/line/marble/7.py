MIN = 0xffff
sol = []
def solution(n, battery):
    global MIN
    arr = []
    for i in battery:
        arr.append(i[0])
    battery_dic = {}
    for j in battery:
        battery_dic[j[0]] = j[1]
    change(0, 0, arr, battery_dic, n)
    print(MIN)
    return MIN

sol = []
MIN = 0xffffff

def change(k, n, arr, battery_dic, N):   # k: 동전수, n: 금액
    global MIN
    if n >= N:
        # sol = [6,6,6,1,1]
        print(sol)
        dict = {}
        for x in sol:
            if x in dict.keys():
                dict[x] += 1
            else:
                dict[x] = 1
        hap = 0
        for y in dict:
            hap += dict[y]*battery_dic[y]
        if hap <= MIN:
            MIN = hap
        return
    for i in range(len(arr)):
        # if arr[i] > n:
        #     continue
        sol.append(arr[i])
        change(k + 1, n + arr[i], arr, battery_dic, N)
        sol.pop()


solution(21, [[6,30000],[3,18000],[4,28000],[1,9500]])