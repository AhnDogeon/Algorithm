import sys
sys.stdin = open("input.txt", "r")

for j in range(1, 11):
    width = int(input())
    building_list = list(map(int, input().split()))
    result = 0
    for i in range(2, width-2):
        for number in range(1, building_list[i]+1):
            if number > building_list[i+1] and number > building_list[i+2] and number > building_list[i-1] and number > building_list[i-2]:
                result += 1
    print(f'#{j} {result}')