def solution(numbers):
    answer = []
    
    N = len(numbers)
    R = 2
    
    visit = [False] * R
    t = [0] * R
    
    def comb(k,s):
        if k == R:
            if sum(t) not in answer:
                answer.append(sum(t))
        else:
            for i in range(s, N + (k-R) + 1):
            # for i in range(s, N):
                t[k] = numbers[i]
                comb(k+1, i+1)
    comb(0, 0)
    
    answer.sort()
    
    return answer

solution([2,1,3,4,1])