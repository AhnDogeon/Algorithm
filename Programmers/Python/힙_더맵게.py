import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while heap[0] < K:
        try:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            heapq.heappush(heap,x + y * 2)
        except IndexError:
            return -1
        answer += 1
    
    return answer


solution([1,2,3,9,10,12], 10)