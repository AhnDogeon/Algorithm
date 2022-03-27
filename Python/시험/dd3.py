final = 0xffff
def solution(A):
    dict = {1:[2,3,4,5],
            2:[1,3,4,6],
            3:[1,2,5,6],
            4:[1,2,5,6],
            5:[1,3,4,6],
            6:[2,3,4,5],}
    def DFS(A, R):
        global final
        cnt = 0
        idx = A[R]
        for j in range(len(A)):
            if A[j] != idx:
                if idx in dict[A[j]]:
                    cnt += 1
                else:
                    cnt += 2
        if cnt < final:
            final = cnt
    for i in range(len(A)):
        DFS(A, i)
    print(final)

solution([1,6,2,3])