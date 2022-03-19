def solution(numbers, hand):
    answer = ''


    board = [[1, 2, 3],[4, 5, 6],[7, 8, 9 ],['*', 0, '#']]

    left = '*'
    right = '#'

    board_dict = {}

    board_dict['*'] = [3, 0]
    board_dict['#'] = [3, 2]

    idx = 1
    for i in range(len(board) - 1):
        for j in range(len(board[0])):
            board_dict[idx] = [i, j]
            idx += 1
    board_dict[0] = [3, 1]

    
    for number in numbers:
        left_idx = board_dict[left]
        right_idx = board_dict[right]
        if number in [1, 4, 7]:
            left = number
            answer += 'L'
        elif number in [3,6,9]:
            right = number
            answer += 'R'
        else:
            left_dis = abs(board_dict[number][0] - board_dict[left][0]) + abs(board_dict[number][1] - board_dict[left][1])
            right_dis = abs(board_dict[number][0] - board_dict[right][0]) +  abs(board_dict[number][1] - board_dict[right][1])
            if left_dis > right_dis:
                right = number
                answer += 'R'
            elif left_dis < right_dis:
                left = number
                answer += 'L'
            elif left_dis == right_dis:
                if hand == "left":
                    left = number
                    answer += 'L'
                else:
                    right = number
                    answer += 'R'

    
    return answer