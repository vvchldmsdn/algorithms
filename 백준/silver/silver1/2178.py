import sys
from pprint import pprint
from collections import deque
sys.stdin = open('2178.txt', 'r')

N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bound_check(x, y):
    return 0 <= x < N and 0 <= y < M


queue = deque()
queue.append((0, 0))

visited = [[N * M + 1] * M for _ in range(N)]
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if bound_check(next_x, next_y) and board[next_x][next_y] != 0:
            if visited[next_x][next_y] > visited[x][y] + 1:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = visited[x][y] + 1

print(visited[N - 1][M - 1])
