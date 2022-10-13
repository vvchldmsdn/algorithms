import sys
from collections import deque
from pprint import pprint
sys.stdin = open('7576.txt', 'r')

M, N = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))


def bound_check(x, y):
    return 0 <= x < N and 0 <= y < M


no_tomato = 0
q = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i, j))
        elif board[i][j] == -1:
            no_tomato += 1

start_num = len(q)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[N * M + 1] * M for _ in range(N)]
for coord in q:
    visited[coord[0]][coord[1]] = 0

while q:
    x, y = q.popleft()
    for d in range(4):
        next_x = x + dx[d]
        next_y = y + dy[d]
        if bound_check(next_x, next_y) and not board[next_x][next_y]:
            if visited[next_x][next_y] > visited[x][y] + 1:
                q.append((next_x, next_y))
                visited[next_x][next_y] = visited[x][y] + 1

ans = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] != N * M + 1:
            ans = max(ans, visited[i][j])
        else:
            cnt += 1

if no_tomato + start_num == N * M:
    print(0)
else:
    if cnt == no_tomato:
        print(ans)
    elif cnt > no_tomato:
        print(-1)
