import datetime
def solution(order_times, k):
    answer = 0
    times = {}
    for i in order_times:
        if i in times.keys():
            times[i] += 1
        else:
            times[i] = 1
    print(times)

    for j in times:
        print(j)
        k = datetime.datetime.strptime(j, '')

        print(times[j])
    return answer


solution(["12:10", "12:20", "12:40", "12:40", "12:50", "13:00", "13:20"], 20)