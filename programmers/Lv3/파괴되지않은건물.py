def solution(board, skill):
    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for type, x1, y1, x2, y2, degree in skill:
        tmp[x1][y1] += degree if type == 2 else -1 * degree
        tmp[x1][y2 + 1] += -1 * degree if type == 2 else degree
        tmp[x2][y1] += -1 * degree if type == 2 else degree
        tmp[x2 + 1][y2 + 1] += degree if type == 2 else -1 * degree

    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i][j + 1] += tmp[i][j]

    for j in range(len(tmp[0]) - 1):
        for i in range(len(tmp) - 1):
            tmp[i + 1][j] += tmp[i][j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [
      [1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
