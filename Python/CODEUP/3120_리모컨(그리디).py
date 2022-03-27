import sys
sys.stdin = open('3120_리모컨(그리디).txt', 'r')

start, end = map(int, input().split())


count = 0

while True:
    if start == end:
        print(count)
        break
    elif start > end:
        if start - 10 >= end:
            if abs(start - 10 - end) > abs(start - 5 - end):
                start -= 5
            else:
                start -= 10
            count += 1
        elif start - 5 >= end:
            if abs(start - 5 - end) > abs(start - 1 - end):
                start -= 1
            elif abs(start - 10 - end) < abs(start - 5 - end):
                start -= 10
            else:
                start -= 5
            count += 1
        elif start - 1 >= end:
            if abs(start - 5 - end) > abs(start - 1 - end):
                start -= 1
            else:
                start -= 5
            count += 1
    elif start < end:
        if start + 10 <= end:
            if abs(start + 10 - end) > abs(start + 5 - end):
                start += 5
            else:
                start += 10
            count += 1
        elif start + 5 <= end:
            if abs(start + 5 - end) > abs(start + 1 - end):
                start += 1
            elif abs(start + 10 - end) < abs(start + 5 - end):
                start += 10
            else:
                start += 5
            count += 1
        elif start + 1 <= end:
            if abs(start + 5 - end) > abs(start + 1 - end):
                start += 1
            else:
                start += 5
            count += 1