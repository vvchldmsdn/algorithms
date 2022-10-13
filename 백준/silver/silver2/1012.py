from pprint import pprint
import sys
sys.stdin = open('1012.txt', 'r')

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bound_check(x, y, i, j):
    return 0 <= x < i and 0 <= y < j


for tc in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]

    for i in range(K):
        row, col = map(int, input().split())
        board[col][row] = 1

    ans = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                board[i][j] = 2
                ans += 1
                stack = [(i, j)]
                while stack:
                    next_x, next_y = stack.pop()
                    for k in range(4):
                        new_x = next_x + dx[k]
                        new_y = next_y + dy[k]
                        if bound_check(new_x, new_y, N, M) and board[new_x][new_y] == 1:
                            board[new_x][new_y] = 2
                            stack.append((new_x, new_y))

    print(ans)
