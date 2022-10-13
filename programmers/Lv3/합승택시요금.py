# def solution(n, s, a, b, fares):
#     answer = 0

#     board = [[0] * (n + 1) for _ in range(n + 1)]
#     for fare in fares:
#         board[fare[0]][fare[1]] = fare[2]
#         board[fare[1]][fare[0]] = fare[2]

#     '''
#     def find_MST(c, n):  c노드에서 n노드까지 가는 MST 가중치 합 찾는 함수

#     answer = 100000 * len(fares)
#     for i in range(1, n + 1):
#         answer = min(find)

#     '''
#     return answer

import heapq
from pprint import pprint


def solution(n, s, a, b, fares):
    answer = 100000 * len(fares)

    link = [[] for _ in range(n + 1)]
    for x, y, z in fares:
        link[x].append((z, y))
        link[y].append((z, x))
    pprint(link)

    def dijkstra(start):
        dist = [987654321] * (n + 1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            value, destination = heapq.heappop(heap)
            if dist[destination] < value:
                continue
            for v, d in link[destination]:
                next_value = value + v
                if dist[d] > next_value:
                    dist[d] = next_value
                    heapq.heappush(heap, (next_value, d))
                    print(start, dist)
        return dist

    dp = [[]] + [dijkstra(i) for i in range(1, n + 1)]
    pprint(dp)

    for i in range(1, n + 1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
      5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
