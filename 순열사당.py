a = [1,5,7]

N = 3

R = 2

def per(k): # 순열
    if k == R:
        print(t)
    else:
        for i in range(N):
            if visit[i]:
                continue
            visit[i] = True
            t[k] = a[i]
            per(k+1)
            visit[i] = False

visit = [False] * N
t = [0] * R
# per(0)

def junbok(k): # 중복 순열
    if k == R:
        print(t)
    else:
        for i in range(N):
            t[k] = a[i]
            junbok(k+1)
print('==============================')
visit = [False] * N
t = [0] * R
# junbok(0)



def comb_r(k, s): # 조합
    if k == R: print(t[0], t[1])
    else:
        for i in range(s, N + (k - R) + 1):
            t[k] = a[i]
            comb_r(k + 1, i + 1)
'''
1 2
1 3
2 3

'''

# comb_r(0,0)


def H_r(k, s): # 중복 조합
    if k == R: print(t)
    else:
        for i in range(s, N):
            t[k] = a[i]
            H_r(k + 1, i)
'''
1 1
1 2
1 3
2 2
2 3
3 3
'''

# H_r(0, 0)

board = []
def bubun(arr, k): # 부분집합
    if k == len(arr):
        # print(arr)
        board.append(arr)
    else:
        bubun(arr, k+1)
        arr.pop(k)
        bubun(arr, k)


#
# bubun(a, 0)
#
# print(board)