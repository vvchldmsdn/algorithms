# from collections import deque
# from heapq import nlargest, heapify


# def getMinimumHealth(initial_players, new_players, rank):
#     result = initial_players[-rank]
#     q = deque(new_players)

#     while q:
#         newp = q.popleft()
#         initial_players.append(newp)
#         heapify(initial_players)
#         result += nlargest(rank, initial_players)[-1]
#     return result


# def getMinimumHealth(initial_players, new_players, rank):
#     players = initial_players + new_players
#     players.sort()

#     new_idx = len(new_players) - 1

#     result = players[-rank]

#     while new_idx >= 0:
#         players.pop(players.index(new_players[new_idx]))
#         new_idx -= 1
#         result += players[-rank]

#     return result


# def getMinimumHealth(initial_players, new_players, rank):
#     players = initial_players + new_players
#     players.sort()
#     for i in range(len(players)):
#         players[i] = str(players[i])

#     new_idx = len(new_players) - 1

#     result = int(players[-rank])

#     while new_idx >= 0:
#         print(players)
#         tmp_idx = players.index(str(new_players[new_idx]))
#         tmp_players = ''.join(players)
#         tmp_players = tmp_players[:tmp_idx] + tmp_players[tmp_idx + 1:]
#         players = list(tmp_players)
#         new_idx -= 1
#         result += int(players[-rank])

#     return result

from pprint import pprint


def getMinimumHealth(initial_players, new_players, rank):
    players = initial_players + new_players
    players.sort()

    new_idx = len(new_players) - 1

    result = players[-rank]

    while new_idx >= 0:
        del players[players.index(new_players[new_idx])]
        new_idx -= 1
        result += players[-rank]

    return result


print(getMinimumHealth([1, 1, 3], [2, 2, 4], 2))
# SELECT T.PARTY
#     ,COUNT(*) AS SEATS_WON

# FROM (SELECTS R.CAN
#             ,C.PARTY
#         FROM (SELECT CONSTITUENCY_ID AS CONS
#                     ,CANDIDATE_ID AS CAN
#                     ,VOTES
#                     ,ROW_NUMBER() OVER(PARTITION BY CONSTITUENCY_ID BY VOTES DESC) AS RN
#             FROM Results
#             ) AS R
#         LEFT JOIN Candidates AS C
#         ON R.CAN = C.ID
#         WHERE R.RN = 1
#         ) AS T
# GROUP BY T.PARTY
# ORDER BY COUNT(*) DESC;
