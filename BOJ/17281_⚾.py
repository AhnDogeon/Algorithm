# import sys
# sys.stdin = open('17281_⚾.txt', 'r')
#
# N = int(input())
#
# board = [list(map(int, input().split())) for _ in range(N)]
#
#
from itertools import permutations
per = permutations([1, 2, 3], 3)
print(list(per))

from itertools import combinations
com = combinations([1, 2, 3], 3)
print(list(com))