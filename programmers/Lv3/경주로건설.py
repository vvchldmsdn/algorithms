from collections import deque
from pprint import pprint


def bound(x, y, n):
    return 0 <= x < n and 0 <= y < n


def solution(board):
    answer = 0
    n = len(board)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = []
    if board[0][1] == 0:
        q.append((0, 1, 0))
        board[0][1] = 100
    if board[1][0] == 0:
        q.append((1, 0, 2))
        board[1][0] = 100

    while q:
        x, y, direction = q.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if bound(nx, ny, n) and board[nx][ny] != 1:  # 범위 안에 들어오고 벽이 아니면
                if d // 2 == direction // 2:  # 방향이 직선이면
                    # 방문했던 적이 없고 새 값이 더 작으면
                    if board[nx][ny] != 0 and board[nx][ny] > board[x][y] + 100:
                        board[nx][ny] = board[x][y] + 100
                        q.append((nx, ny, d))
                    elif board[nx][ny] == 0:
                        board[nx][ny] = board[x][y] + 100
                        q.append((nx, ny, d))
                else:  # 방향이 꺽이면
                    if board[nx][ny] != 0 and board[nx][ny] > board[x][y] + 600:  # //
                        board[nx][ny] = board[x][y] + 600
                        q.append((nx, ny, d))
                    elif board[nx][ny] == 0:
                        board[nx][ny] = board[x][y] + 600
                        q.append((nx, ny, d))
    # pprint(board)
    return board[-1][-1]


print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [
      1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
