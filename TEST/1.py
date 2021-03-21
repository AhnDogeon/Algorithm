def solution(table, languages, preference):
    answer = []
    jobs = {}
    for job in table:
        a = job.split()
        jobs[a[0]] = a[1:]

    score = [5,4,3,2,1]
    maxH = 0
    for item, value in jobs.items():
        total = 0
        for language in range(len(languages)):
            try:
                idx = value.index(languages[language])
                total += (score[idx] * preference[language])
            except:
                continue
        print(total)
        if total > maxH:
            maxH = total
            answer = item
        elif total == maxH:
            if item < answer:
                answer = item
    return answer


# print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
#          ["PYTHON", "C++",  "SQL"], [7,5,5]))

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
               ["JAVA", "JAVASCRIPT"], [7, 5]))