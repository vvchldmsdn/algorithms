import sys
from itertools import combinations
from copy import deepcopy
sys.stdin = open('2.txt', 'r')


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    info = []
    for i in range(N):
        info.append(list(map(int, input().split())))

    for i in range(len(info)):
        info[i][0] += 15
        info[i][1] += 15

    for i in range(len(info)):
        info[i].append(0)  # 마지막에 visited인지 추가

    num_chargers = 1

    ans = 100

    while num_chargers < 3:
        if num_chargers == 1:
            for i in range(31):
                for j in range(31):
                    visited = 0
                    for k in range(len(info)):
                        if not info[k][3]:
                            if dist((i, j), (info[k][0], info[k][1])) <= info[k][2]:
                                visited += 1
                    if N == visited:
                        tmp_ans = 0
                        for k in range(len(info)):
                            tmp_ans += dist((i, j), (info[k][0], info[k][1]))
                    ans = min(ans, tmp_ans)
        if ans != 100:
            break

    print(ans)

# def distance(a, b, c, d):
#     return abs(a - b) + abs(c - d)


# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())  # 집 갯수

#     ans = 100
#     info = []
#     for i in range(N):
#         info.append(list(map(int, input().split())))

#     for i in range(len(info)):
#         info[i][0] += 15
#         info[i][1] += 15

#     combi_base = []
#     for i in range(12, 20):
#         for j in range(12, 20):
#             combi_base.append((i, j))

#     coord_combi = list(combinations(combi_base, 2))

#     not_reached = 0
#     reached = 0
#     for combi in coord_combi:  # ((0,0), (0,1))
#         tmp_homes = deepcopy(info)

#         tmp_ans = 0

#         checked_idx = []
#         for coord in combi:  # (0, 0)
#             for i in range(len(tmp_homes)):  # [0,0,0]
#                 if i not in checked_idx:
#                     if distance(tmp_homes[i][0], coord[0], tmp_homes[i][1], coord[1]) <= tmp_homes[i][2]:
#                         # print('coord', coord)
#                         checked_idx.append(i)
#                         tmp_ans += distance(tmp_homes[i][0],
#                                             tmp_homes[i][1], coord[0], coord[1])

#         if len(checked_idx) == N:
#             print('combi', combi)
#             print('tmp_ans', tmp_ans)
#             ans = min(ans, tmp_ans)
#             reached += 1
#         else:
#             not_reached += 1

#     print(reached)
#     print(ans)
