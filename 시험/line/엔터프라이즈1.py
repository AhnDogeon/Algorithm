# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = 'adfkdncjdk'
answer = 0
if len(user_input) >= 10:
    answer += 1

banbok = [False, False, False, False]  # 소문자, 대문자, 숫자, 특수문자

asc_list = []
for i in user_input:
    asc_list.append(ord(i))
print(asc_list)

for j in asc_list:
    if banbok[3] == False:
        if 33 <= j <= 47 or 58 <= j <= 64 or 91 <= j <= 96 or 123 <= j <= 125:  # 특수문자
            banbok[3] = True

    if banbok[0] == False:
        if 97 <= j <= 122:
            banbok[0] = True
    if banbok[1] == False:
        if 65 <= j <= 90:
            banbok[1] = True
    if banbok[2] == False:
        if 48 <= j <= 57:
            banbok[2] = True

answer = answer + banbok.count(True)
print(banbok)
print('LEVEL' + str(answer))