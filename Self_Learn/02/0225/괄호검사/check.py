import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    string = input()
    result_list = []
    result = 0
    for i in string:
        if i == '(' or i == '{' or i == '[':
            result_list.append(i)
        if i == ')':
            if len(result_list) != 0 and result_list[-1] == '(':
                result_list.pop(-1)
            else:
                result = 0
                break
        elif i == '}':
            if len(result_list) != 0 and result_list[-1] == '{':
                result_list.pop(-1)
            else:
                result = 0
                break
        elif i == ']':
            if len(result_list) != 0 and result_list[-1] == '[':
                result_list.pop(-1)
            else:
                result = 0
                break
    else:
        if len(result_list) == 0:
            result = 1

    print(f'#{test_case} {result}')