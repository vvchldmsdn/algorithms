# import sys
# sys.stdin = open('3.txt', 'r')


# def is_bound(x, y, N):
#     if x == 0 or x == N - 1 or y == 0 or y == N - 1:
#         return 1
#     else:
#         return 0


# def check(x, y, m, N):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, 1, -1]

#     ans = N + 1
#     min_d = 0
#     for i in range(4):
#         xd = dx[i]
#         yd = dy[i]

#         tmp_x = x
#         tmp_y = y
#         while m[tmp_x][tmp_y] == 0 and 0 <= tmp_x < N and 0 <= tmp_y < N:
#             tmp_x += xd
#             tmp_y += yd

#         if is_bound(tmp_x, tmp_y, N):
#             tmp_ans = abs(tmp_x - x) + abs(tmp_y - y)
#             if tmp_ans < ans


# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())

#     board = []
#     for i in range(N):
#         board.append(list(map(int, input().split())))

#     for layer in range((N + 1) // 2):
#         for i in range(N):
#             for j in range(N):
