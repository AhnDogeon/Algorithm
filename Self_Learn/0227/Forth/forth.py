import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    lst = list(map(str, input().split()))
    stack = []

    for i in range(len(lst)):
        if lst[i] == '+':
            if len(stack) < 2:
                print(f'#{t} error')
                break
            num = stack[-2] + stack[-1]
            stack.pop(-1)
            stack.pop(-1)
            stack += [int(num)]

        elif lst[i] == '-':
            if len(stack) < 2:
                print(f'#{t} error')
                break
            num = stack[-2] - stack[-1]
            stack.pop(-1)
            stack.pop(-1)
            stack += [int(num)]

        elif lst[i] == '*':
            if len(stack) < 2:
                print(f'#{t} error')
                break
            num = stack[-2] * stack[-1]
            stack.pop(-1)
            stack.pop(-1)
            stack += [int(num)]

        elif lst[i] == '/':
            if len(stack) < 2:
                print(f'#{t} error')
                break

            elif stack[-1] == 0:
                print(f'#{t} error')
                break

            elif stack[-1] != 0:
                num = stack[-2] / stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack += [int(num)]

        elif lst[i] == '.':
            if len(stack) > 1:
                print(f'#{t} error')

            else:
                print(f'#{t} {"".join(list(map(str, stack)))}')

        elif type(int(lst[i])) is int:
            stack += [int(lst[i])]
