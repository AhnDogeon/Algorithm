import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    new_list=[]
    for number in range(0, 2*N, 2):
        new_list.append(arr[number:number+2])

    final_result=[new_list[0]]
    for a in range(len(new_list)):
        for x in new_list:
            if x[1] == final_result[0][0]:
                final_result.insert(0, x)
    for b in range(len(new_list)):
        for y in new_list:
            if y[0] == final_result[-1][-1]:
                final_result.append(y)

    print(f'#{test_case}', end=' ')
    for final_x in range(len(final_result)):
        for final_y in final_result[final_x]:
            print(f'{final_y }', end=' ')
    print()