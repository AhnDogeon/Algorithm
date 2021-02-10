N = 3

a = [1, 2, 3]

R = 2

visit = [False] * R
t = [0] * R


def com(k, s):
    if k == R:
        print(t)
    else:
        for i in range(s, N + (k-R) + 1):
        # for i in range(s, N):
            t[k] = a[i]
            com(k+1, i+1)


com(0, 0)