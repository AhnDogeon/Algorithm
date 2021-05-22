import copy
import sys
sys.stdin = open('input.txt', 'r')


for test_case in range(1, 11):
    V, E = map(int, input().split())
    graph = list(map(int, input().split()))
    two_graph = []
    for i in range(0, len(graph) - 1, 2):
        two_graph.append(graph[i:i + 2])

    count_list = []
    for zero in range(V + 1):
        count_list.append(0)
    for x in range(V + 1):
        for y in two_graph:
            if x == y[1]:
                count_list[x] += 1
    # print(two_graph)
    # print(count_list)

    result_list = []
    while len(two_graph) >= 0:
        copy_graph = copy.deepcopy(two_graph)
        for a in range(1, len(count_list)):
            if count_list[a] == 0:
                for number in range(len(copy_graph)):
                    if copy_graph[number][0] == a:
                        result_list.append(copy_graph[number])
                        count_list[a] -= 1
                        two_graph.remove(copy_graph[number])
        for b in result_list:
            for c in copy_graph:
                if b[1] == c[0]:
                    count_list[copy_graph.index(c)] -= 1

    print(result_list)