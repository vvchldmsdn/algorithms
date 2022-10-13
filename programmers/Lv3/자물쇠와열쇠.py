from pprint import pprint


def cal(a, b, x, y, n):
    for i in range(n):
        for j in range(n):
            if a[i][j] + b[i + x][j + y] == 2 or a[i][j] + b[i + x][j + y] == 0:
                return False
    return True


def rotate_cw(a):
    result = list(map(list, zip(*a[::-1])))
    return result


def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_key = [[0] * (2 * n + m) for _ in range(2 * n + m)]
    for i in range(n, m + n):
        for j in range(n, m + n):
            new_key[i][j] = key[i - n][j - n]

    rotate_cnt = 0
    while rotate_cnt < 4:
        for i in range(n + m + 1):
            for j in range(n + m + 1):
                if cal(lock, new_key, i, j, n):
                    return True
        lock = rotate_cw(lock)
        rotate_cnt += 1

    return False


print(solution([[1, 0], [0, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


# print(cal([[1, 0, 1], [1, 1, 0], [1, 1, 1]], [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#                                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                                               [0, 0, 0, 1, 0, 0, 0, 0, 0],
#                                               [0, 0, 0, 0, 1, 1, 0, 0, 0],
#                                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                                               [0, 0, 0, 0, 0, 0, 0, 0, 0]], 4, 2, 3))
