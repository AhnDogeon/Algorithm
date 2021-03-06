arr = "ABCDE"
pick = []
n = len(arr)
r = 4


def comb(k, start):
    if k == r:
        print(pick)
        return

    for i in range(start, n):
        pick.append(arr[i])
        comb(k + 1, i + 1)
        pick.pop()


comb(0, 0)

