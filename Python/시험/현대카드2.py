
left = 11
right = 20
offset = 210
answer = ''
flag = True

num_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
eng_lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
           'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

while flag:

    if len(answer) >= right:
        flag = False
        result = answer[left-1:right]
        print(result)

    else:
        check = len(str(offset))
        num = str(offset)

        while check:
            print('------check--------')
            print(check)

            if len(num) >= 2 and num[0:2] in num_lst:
                print('here22222222222222222')
                check_num = num[0:2]
                print('----------checknum----------------')
                print(check_num)
                num = num[2:]
                print('---------new num-----------------')
                print(num)
                check -= 2

            else:
                print('here111111111111111111111')
                check_num = num[0]
                print('----------checknum----------------')
                print(check_num)
                num = num[1:]
                print('---------new num-----------------')
                print(num)
                check -= 1

            idx = num_lst.index(check_num)
            print('----------idx----------------')
            print(idx)
            answer += eng_lst[idx]

            print('----------answer----------------')
            print(answer)
            print('----------finish----------------')
        print('----------offset----------------')
        offset += 1




