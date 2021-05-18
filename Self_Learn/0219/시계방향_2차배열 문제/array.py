arr = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14],
]
maxH = 0
minH = arr[0][0]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] > maxH:
            maxH = arr[i][j]
        if arr[i][j] < minH:
            minH = arr[i][j]


number = minH
while number < maxH + 1:
    if 1 <= number < 6:
        i = 0
        for j in range(5):
            arr[i][j] = number
            number += 1
    if 6 <= number < 10:
        j = 4
        for i in range(1, 5):
            arr[i][j] = number
            number += 1
    if 10 <= number < 14:
        i = 4
        for j in range(3, -1, -1):
            arr[i][j] = number
            number += 1
    if 14 <= number < 17:
        j = 0
        for i in range(3, 0, -1):
            arr[i][j] = number
            number += 1
    if 17 <= number < 20:
        i = 1
        for j in range(1, 4):
            arr[i][j] = number
            number += 1
    if 20 <= number < 22:
        j = 3
        for i in range(2, 4):
            arr[i][j] = number
            number += 1
    if 22 <= number < 24:
        i = 3
        for j in range(2, 0, -1):
            arr[i][j] = number
            number += 1
    if 24 <= number:
        i = 2
        for j in range(1, 3):
            arr[i][j] = number
            number += 1

print(arr)