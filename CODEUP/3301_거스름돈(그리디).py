import sys
sys.stdin = open('3301_거스름돈(그리디).txt', 'r')

n = int(input())

money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

cnt_list = []
for _ in range(len(money_list)):
    cnt_list.append(0)


for x in range(len(money_list)):
    if n >= money_list[x]:
        cnt_list[x] += int(n / money_list[x])
        n -= (money_list[x] * cnt_list[x])
print(sum(cnt_list))