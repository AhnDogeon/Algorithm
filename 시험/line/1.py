import sys
sys.stdin = open('1.txt', 'r')
messages, consumers = map(int, input().strip().split(' '))


time_list = []
consumer_list = [[] for c in range(consumers)]

for _ in range(messages):
    time_list.append(int(input()))


time = 1
while time_list:
    for j in range(len(consumer_list)):
        if consumer_list[j] != [] and time > consumer_list[j]:
            consumer_list[j] = []
    for i in range(len(consumer_list)):
        if consumer_list[i] == [] and time_list:
            consumer_list[i] = time_list.pop(0) + time - 1
    time += 1

print(max(consumer_list))
