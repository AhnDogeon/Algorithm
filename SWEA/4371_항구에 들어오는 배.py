import sys
sys.stdin = open('4371_항구에 들어오는 배.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    line = []
    for n in range(N):
        line.append(int(input()))

    result = []
    cnt = 0
    while line:
        if len(line) <= 1:
            break
        result = []
        minus = line[1] - line[0]
        total = line[0] + minus
        while total in line:
            if total in line:
                result.append(total)
                if len(result) == line.count(result[0]):
                    while result:
                        if result[0] in line:
                            line.remove(result[0])
                            result.pop()
            if len(result) == 0:
                total = total + minus
        cnt += 1
    if cnt == 0:
        cnt += 1
    print('#{} {}'.format(test_case, cnt))
