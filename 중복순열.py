'==================== 라이브러리 순열, 중복순열, 조합, 중복조합 ========================='
from itertools import permutations
per = permutations([1,2,3],2)
print(list(per))
#[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from itertools import product
per = product([1,2,3],repeat=2)
print(list(per))
#[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


from itertools import combinations
print(list(combinations([1,2,3],2) ) )
#[(1, 2), (1, 3), (2, 3)]

from itertools import combinations_with_replacement
print( list ( combinations_with_replacement([1,2,3],2) ) )
#[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]


print('--------------------------------------------------------')

'==================== 순열 ========================='
def perm_i():
    for i1 in range(1, N + 1):
        for i2 in range(1, N + 1):
            if i2 != i1:
                print(i1, i2)
'''
1 2
1 3
2 1
2 3
3 1
3 2
'''

def perm_r(k):
    if k == R :
        print(t[0], t[1])
    else:
        for i in range(N):
            if visited[i]: continue
            t[k] = i + 1
            visited[i] = 1
            perm_r(k + 1)
            visited[i] = 0
'''
1 2
1 3
2 1
2 3
3 1
3 2
'''


'==================== 조합 ========================='


def comb_i():
    for i in range(N - 1):
        for j in range(i + 1, N):
            print(a[i], a[j])

'''
1 2
1 3
2 3
'''

def comb_r(k, s):
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


'===================== 중복 순열 ========================='

def pi_i():
    for i in range(N):
        for j in range(N):
            print(a[i], a[j])

'''
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
'''

def pi_r(k):
    if k == R: print(t[0], t[1])
    else:
        for i in range(N):
            t[k] = a[i]
            pi_r(k + 1)

'''
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
'''


'====================== 중복 조합 ========================'

def H_i():
    for i in range(N):
        for j in range(i, N):
            print(a[i], a[j])

'''
1 1
1 2
1 3
2 2
2 3
3 3
'''

def H_r(k, s):
    if k == R: print(t[0], t[1])
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

'====================== 호출 ========================'
N = 3
R = 2
a = [1, 2, 3]
t = [0] * R


# t = [0] * N
visited = [0] * N
print()
print("순열")
perm_i()
print("----------")
perm_r(0)
print("----------")

print()
print('조합')
comb_i()
print("----------")
comb_r(0, 0)

print()
print("중복 순열")
pi_i()
print("----------")
pi_r(0)

print()
print("중복 조합")
H_i()
print("----------")
H_r(0, 0)
print('==========부분집합======================')

a = [1, 2, 3, 4]
R = len(a)
t = [0] * R


def bubun(k):
    if k == R:
        result = []
        for j in range(len(t)):
            if t[j] == 1:
                result.append(a[j])
        print(result)
    else:
        for i in range(2):
            t[k] = i
            bubun(k+1)

bubun(0)