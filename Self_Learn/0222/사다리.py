import sys
sys.stdin = open("input.txt", "r")



for t in range(1, 11):
   x = input()
   num = []
   for i in range(100):
       num.append([0]+list(map(int, input().split()))+[0])

   last = num[99].index(2)

   idx = [99, last]
   x = idx[0]
   y = idx[1]
   while 0 < x <= 100 and 0 < y <= 100:
       if num[x][y - 1] == 1 and y - 1 != res:
           res = y
           y = y - 1

       if num[x][y + 1] == 1 and y + 1 != res:
           res = y
           y = y + 1

       if num[x-1][y] == 1:
           res = y
           x = x - 1


   print(f'#{t} {y-1}')