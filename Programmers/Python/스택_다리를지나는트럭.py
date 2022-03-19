# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     bridge = [0] * bridge_length
#
#     while (truck_weights):
#         print(truck_weights)
#         time += 1
#         # 한 칸씩 이동
#         for i in range(len(bridge) - 1, -1, -1):
#             if bridge[i]:
#                 if i == bridge_length -1:
#                     bridge[i] = 0
#                 else:
#                     bridge[i + 1] = bridge[i]
#                     bridge[i] = 0
#         # 다음 트럭이 들어올 수 있는지 체크
#         if sum(bridge) + truck_weights[0] <= weight:
#             truck = truck_weights.pop(0)
#             bridge[0] = truck
#
#     time = time + bridge_length
#     return time
#
#
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    while len(bridge) != 0:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time


print(solution(2, 10, [7,4,5,6]))