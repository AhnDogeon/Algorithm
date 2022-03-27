from itertools import permutations

arr = list(map(int,input().split()))
n = len(arr)
ind = int(input())

permu = permutations(arr,n)
permu = list(permu)
dap = []


for i in range(len(permu)):
    arr1 = list(permu[i])
    arr2 = ''.join(map(str, arr1))
    dap.append(int(arr2))

dap = sorted(dap)

chl = ''
real = dap[ind-1]
real = str(real)

if len(real) < n:
    zero = n - len(real)

    for _ in range(zero):
        chl += '0'
    print(chl+real)
else:
    print(real)
