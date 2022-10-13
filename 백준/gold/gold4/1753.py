import sys
from collections import deque
sys.stdin = open('1753.txt', 'r')

V, E = map(int, input().split())
K = int(input())
matr = dict()
for i in range(V):
    matr[i + 1] = dict()

for i in range(E):
    u, v, w = map(int, input().split())
    if v not in matr[u]:
        matr[u][v] = [w]
    else:
        matr[u][v].append(w)
        matr[u][v].sort()

visited = [11 * V] * (V + 1)
visited[K] = 0

q = deque()
q.append(K)

while q:
    x = q.popleft()
    for node in matr[x]:
        if visited[node] > visited[x] + matr[x][node][0]:
            q.append(node)
            visited[node] = visited[x] + matr[x][node][0]
            print(visited)

for total in visited[1:]:
    if total == 11 * V:
        print('INF')
    else:
        print(total)
