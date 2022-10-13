def solution(triangle):
    dim = len(triangle)
    board = [[0] * dim for _ in range(dim)]
    for i in range(dim):
        for j in range(len(triangle[i])):
            board[i][j] = triangle[i][j]

    board[1][0] = board[1][0] + board[0][0]
    board[1][1] = board[1][1] + board[0][0]

    for i in range(2, dim):
        for j in range(i + 1):
            if j == 0:
                board[i][j] = board[i - 1][j] + board[i][j]
            elif j == i:
                board[i][j] = board[i - 1][i - 1] + board[i][j]
            else:
                board[i][j] = max(board[i - 1][j - 1],
                                  board[i - 1][j]) + board[i][j]

    # print(board)

    answer = max(board[-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
