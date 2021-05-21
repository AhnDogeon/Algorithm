import sys
sys.stdin = open('input.txt', 'r')

# 컴공 도움을 받았습니다 너무 어렵습니다...
def win(x, y):
    if (lst[x-1] == 1 and lst[y-1] == 3) or (lst[x-1] == 1 and lst[y-1] == 1):
        return x
    elif (lst[x-1] == 2 and lst[y-1] == 1) or (lst[x-1] == 2 and lst[y-1] == 2):
        return x
    elif (lst[x-1] == 3 and lst[y-1] == 2) or (lst[x-1] == 3 and lst[y-1] == 3):
        return x
    return y

def match(start, end):
    if start == end:
        return start

    first_value = match(start, (start+end)//2)
    second_value = match((start+end)//2+1, end)
    return win(first_value, second_value)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    start = 1
    end = N
    print(f'#{test_case} {match(start, end)}')