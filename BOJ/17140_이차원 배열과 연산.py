import sys
sys.stdin = open('17140_이차원 배열과 연산.txt', 'r')

R, C, K = map(int, input().split())


arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))
# print(arr)



t = 0
while t < 101:
    if R - 1 < len(arr) and C - 1 < len(arr[0]) and arr[R-1][C-1] == K:
        print(t)
        break
    else:
        if len(arr) >= len(arr[0]): # 행길이가 열길이보다 길 때 : R 연산
            max_len = 0
            real_list = []
            for i in range(len(arr)):
                result = set()
                for j in range(len(arr[i])):
                    if arr[i][j] != 0:
                        result.add((arr[i][j], arr[i].count(arr[i][j])))

                result = sorted(result, key=lambda result: result[0])
                result = sorted(result, key=lambda result: result[1])

                if len(result) >= max_len:
                    max_len = len(result)
                real = []
                for (a, b) in result:
                    real.append(a)
                    real.append(b)
                real_list.append(real)

            for k in range(len(real_list)):
                if len(real_list[k]) < max_len * 2:
                    real_list[k].extend([0] * ((max_len * 2) - len(real_list[k])))
            arr = real_list
            if len(arr[0]) > 100:
                for m in range(len(arr)):
                    arr[m] = arr[m][0:100]
            t += 1
        elif len(arr) < len(arr[0]):  # 열길이가 행길이보다 길 때 : C 연산
            max_len = 0
            real_list = []
            for i in range(len(arr[0])):
                result = set()
                for j in range(len(arr)):
                    if arr[j][i] != 0:
                        result.add(arr[j][i])


                real = []
                for k in result:
                    cnt = 0
                    for n in range(len(arr)):
                        if k == arr[n][i]:
                            cnt += 1
                    real.append((k, cnt))
                real = sorted(real, key=lambda real: real[0])
                real = sorted(real, key=lambda real: real[1])

                if len(real) >= max_len:
                    max_len = len(real)

                real_2 = []
                for (a, b) in real:
                    real_2.append(a)
                    real_2.append(b)
                real_list.append(real_2)

            for k in range(len(real_list)):
                if len(real_list[k]) < max_len * 2:
                    real_list[k].extend([0] * ((max_len * 2) - len(real_list[k])))

            final_list = [[] for _ in range(len(real_list[0]))]

            for q in range(len(real_list[0])):
                fake_list = []
                for w in range(len(real_list)):
                    fake_list.append(real_list[w][q])
                final_list[q] = fake_list

            arr = final_list
            if len(arr) > 100:
                arr = arr[0:101]
            t += 1
if t > 100:
    print(-1)