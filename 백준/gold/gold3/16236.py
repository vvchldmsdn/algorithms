import sys
from collections import deque
sys.stdin = open('16236.txt', 'r')


def bound(N, i, j):
    return 0 <= i < N and 0 <= j < N


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

pos = ()
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            pos = (i, j)
            break
    if pos != ():
        break

board[pos[0]][pos[1]] = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

answer = 0

ate = 0
size = 2

while True:
    q = deque()
    q.append((pos, 0))
    tmp = []
    visited = [[0] * N for _ in range(N)]
    visited[pos[0]][pos[1]] = 1
    while q:
        position, move = q.popleft()
        if board[position[0]][position[1]] != 0 and board[position[0]][position[1]] < size:
            if move != 0:
                tmp.append((position[0], position[1], move))

        for d in range(4):
            nx = position[0] + dx[d]
            ny = position[1] + dy[d]
            if bound(N, nx, ny) and board[nx][ny] <= size:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append(((nx, ny), move + 1))

    if tmp != []:
        tmp.sort(key=lambda x: (
            x[2], x[0], x[1]))
        pos = (tmp[0][0], tmp[0][1])
        # print(pos)
        board[tmp[0][0]][tmp[0][1]] = 0
        answer += tmp[0][2]
        # print(answer)
        ate += 1
        if ate == size:
            ate = 0
            size += 1
        # print(tmp)
    else:
        break
    # print('-----------------')
print(answer)
