# import sys
# from pprint import pprint
# sys.stdin = open("1.txt", "r")


# def bound_check(i, j, w, h):
#     return 0 <= i < w and 0 <= j < h


# T = int(input())

# for tc in range(1, T + 1):
#     W, H = map(int, input().split())

#     visited = [[False] * W for _ in range(H)]
#     board = []

#     for _ in range(H):
#         board.append(list(map(int, input().split())))

#     dy_odd = [-1, 1, 0, 0, 1, 1]  # 행
#     dx_odd = [0, 0, -1, 1, -1, 1]  # 열

#     dy_even = [-1, 1, 0, 0, -1, -1]
#     dx_even = [0, 0, -1, 1, -1, 1]

#     for i in range(W):
#         for j in range(H):
#             if not i % 2:  # 짝수 열 일때
