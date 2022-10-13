import sys
from pprint import pprint
sys.stdin = open("2667.txt", 'r')


def bound_check(x, y):
    return 0 <= x < N and 0 <= y < N


N = int(input())

board = []
for i in range(N):
    board.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

num_group = 0
num_aparts = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            num_group += 1
            num_aparts.append(1)

            board[i][j] = 2
            stack = [(i, j)]
            while stack:
                next_x, next_y = stack.pop()
                for d in range(4):
                    new_x = next_x + dx[d]
                    new_y = next_y + dy[d]
                    if bound_check(new_x, new_y) and board[new_x][new_y] == 1:
                        board[new_x][new_y] = 2
                        stack.append((new_x, new_y))
                        num_aparts[-1] += 1


num_aparts.sort()
print(num_group)
for i in range(len(num_aparts)):
    print(num_aparts[i])
