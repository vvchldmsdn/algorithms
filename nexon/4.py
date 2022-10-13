# SELECT T.PARTY
#     ,COUNT(*) AS SEATS_WON

# FROM (SELECT R.CAN
#             ,C.PARTY
#         FROM (SELECT CONSTITUENCY_ID AS CONS
#                     ,CANDIDATE_ID AS CAN
#                     ,VOTES
#                     ,ROW_NUMBER() OVER(PARTITION BY CONSTITUENCY_ID ORDER BY VOTES DESC) AS RN
#             FROM Results
#             ) AS R
#         LEFT JOIN Candidates AS C
#         ON R.CAN = C.ID
#         WHERE R.RN = 1
#         ) AS T
# GROUP BY T.PARTY
# ORDER BY COUNT(*) DESC;
