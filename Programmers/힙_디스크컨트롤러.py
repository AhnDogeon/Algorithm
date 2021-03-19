import heapq

def solution(jobs):
    print(jobs)
    heap = []

    for i, j in jobs:
        heapq.heappush(heap, [j, i])

    time = 0
    answer = []
    while heap:
        minH = heapq.heappop(heap)
        if time >= minH[1]:
            time += minH[0]
            answer.append(time - minH[1])
        else:
            heapq.heappush(heap, minH)
            time += 1
    print(answer)
    return int(sum(answer) / len(jobs))

print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))