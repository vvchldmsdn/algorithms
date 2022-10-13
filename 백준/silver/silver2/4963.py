import sys
sys.stdin = open('4963.txt', 'r')

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]


def bound_check(x, y, w, h):
    return 0 <= x < h and 0 <= y < w


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))

    ans = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    board[x][y] = 2
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if bound_check(nx, ny, w, h) and board[nx][ny] == 1:
                            stack.append((nx, ny))
                ans += 1

    print(ans)
