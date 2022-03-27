def solution(blocks):
    answer = []
    print(blocks)


    arr = []
    for i in range(len(blocks)):
        virtual_arr = ['' for _ in range(i + 1)]
        virtual_arr[blocks[i][0]] = blocks[i][1]
        print(virtual_arr)
        answer.append(virtual_arr)
    print(arr)

    return answer


solution([[0, 50],[0,22],[2,10],[1,4],[4,-13]])

