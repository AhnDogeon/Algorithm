def solution(jobs):
    jobs = sorted(jobs, key=lambda x:x[1])
    print(jobs)
    result = len(jobs)
    time = 0
    answer = []
    while len(jobs) != 0:
        for job in jobs:
            if time >= job[0]:
                time += job[1]
                answer.append(time - job[0])
                jobs.pop(jobs.index(job))
                break
        else:
            time += 1

    return int(sum(answer) / result)

print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))