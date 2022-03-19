#### Version 1
def solution(numbers):
    answer = ''
    arr = []
    for i in numbers:
        original = i
        temp = i
        while temp < 1000:
            temp = int(str(temp) + str(i))
        arr.append([temp, original])
    arr.sort(key=lambda x:x[0], reverse=True)
    for item in arr:
        answer += str(item[1])
    return answer


#### Version 2
def solution(num):
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(num)))

다]