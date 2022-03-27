import sys
sys.stdin = open('3.txt', 'r')

people = int(input())

arr = []
for _ in range(people):
    a, b = map(int, input().strip().split(' '))
    arr.append([a, b])

maxtime = max(arr)[1]

time = 0
max_answer = 0
while time <= maxtime:
    answer = 0
    # i = [시작, 끝]
    for i in arr:
        if time >= i[0] and time < i[1]:
            answer += 1
    if answer > max_answer:
        max_answer = answer
    time += 1

print(max_answer)