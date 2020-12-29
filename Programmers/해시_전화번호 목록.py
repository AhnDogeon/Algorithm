def solution(phone_book):
    answer = True
    dict_phonebook = {}
    phone_book.sort()
    for i in range(len(phone_book)):
        if i == 0:
            continue
        if phone_book[i-1] in phone_book[i]:
            answer = False
            return answer
    return answer

print(solution(['119', '97674223', '1195524421']))
