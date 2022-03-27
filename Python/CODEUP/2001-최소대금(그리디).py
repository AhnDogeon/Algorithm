import sys

sys.stdin = open('2001-최소대금(그리디).txt', 'r')

first_pasta = int(input())
second_pasta = int(input())
third_pasta = int(input())

first_juice = int(input())
second_juice = int(input())

pasta_list = [first_pasta, second_pasta, third_pasta]
juice_list = [first_juice, second_juice]

print(round((min(pasta_list) + min(juice_list)) * 1.1, 1))