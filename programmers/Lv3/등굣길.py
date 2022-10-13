def solution(m, n, puddles):
    puddles = [[p, q] for [q, p] in puddles]
    board = [[0] * m for _ in range(n)]
    board[0][0] = 1

    for i in range(n):
        for j in range(m):
            if [i + 1, j + 1] not in puddles:
                if i - 1 >= 0:
                    board[i][j] += board[i - 1][j]
                if j - 1 >= 0:
                    board[i][j] += board[i][j - 1]
                board[i][j] %= 1000000007

    return board[-1][-1]


print(solution(4, 3, [[2, 2]]))
print(solution(7, 6, [[1, 4], [3, 5], [4, 1]]))
