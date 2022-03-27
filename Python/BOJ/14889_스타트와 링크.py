import sys
sys.stdin = open('14889_스타트와 링크.txt', 'r')

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]


arr = [i + 1 for i in range(N)]
pick = []
n = len(arr)
r = N / 2

maxH = 0xffff

result = []
total_pick = 0
total_pick2 = 0
def per(k, start, varr, perr, what):
    global total_pick, total_pick2
    if k == perr:
        # print(result)
        if what == 1:
            total_pick += board[result[0]-1][result[1]-1]
        elif what == 2:
            total_pick2 += board[result[0] - 1][result[1] - 1]
        return

    for j in range(start, len(varr)):
        if varr[j] not in result:
            result.append(varr[j])
            per(k+1, 0, varr, perr, what)
            result.pop()



def comb(k, start):
    global maxH, pick, total_pick, total_pick2
    if k == r:
        pick2 = []
        for m in range(N):
            if arr[m] not in pick:
                pick2.append(arr[m])

        # print(pick)
        # print(pick2)
        total_pick = 0
        per(0, 0, pick, 2, 1)
        # print(total_pick)
        # print('------------------------')
        total_pick2 = 0
        per(0, 0, pick2, 2, 2)
        # print(total_pick2)
        # print('========================================')

        if maxH > abs(total_pick-total_pick2):
            maxH = abs(total_pick-total_pick2)
        total_pick2 = 0
        total_pick = 0

        return

    for i in range(start, n):
        pick.append(arr[i])
        comb(k + 1, i + 1)
        pick.pop()


comb(0, 0)

print(maxH)