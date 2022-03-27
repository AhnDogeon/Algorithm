def soultion(target, positions):
    for i in range(len(target)-1):
        target[i+1] = target[i] + target[i+1]

    for i in range(len(target)):
        target[i] = target[i] ** 2

    real_positions = []
    for j in range(len(positions)):
        real_positions.append(positions[j][0] ** 2 + positions[j][1] ** 2)


    point = 0
    for j in range(len(real_positions)):
        if 0 <= real_positions[j] <= target[0]:
            point += 10
        elif target[0] < real_positions[j] <= target[1]:
            point += 8
        elif target[1] < real_positions[j] <= target[2]:
            point += 6
        elif target[2] < real_positions[j] <= target[3]:
            point += 4
        elif target[3] < real_positions[j] <= target[4]:
            point += 2
        elif target[4] < real_positions[j]:
            point += 0
    return point

soultion([2, 2, 2, 2, 2]  , [[0, 0], [0, 1], [1, 1], [-3, 5], [7,5], [10, 0], [-15, 22], [-6, -5], [3, 3], [5, -5]]) # 답 54점
soultion([2, 3, 4, 3, 2]  , [[0, 0], [0, 1], [1, 1], [-3, 5], [7,5], [10, 0], [-15, 22], [-6, -5], [3, 3], [5, -5]]) # 잡 66점