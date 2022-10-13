def bound_check(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def solution(n, m, x, y, r, c, k):
    if k < abs(x - r) + abs(y - c):
        return 'impossible'

    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    q = [(x-1, y-1, 0, '')]
    while q:
        i, j, move, word = q.pop()
        if move == k and (i, j) == (r-1, c-1):
            return word

        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]
            if abs(ni - (r-1)) + abs(nj - (c-1)) > k - move - 1:
                continue
            if bound_check(ni, nj, n, m) and move < k:

                if d == 0:
                    q.append((ni, nj, move+1, word + 'u'))
                elif d == 1:
                    q.append((ni, nj, move+1, word + 'r'))
                elif d == 2:
                    q.append((ni, nj, move+1, word + 'l'))
                elif d == 3:
                    q.append((ni, nj, move+1, word + 'd'))
    return 'impossible'


print(solution(3, 4, 2, 3, 3, 1, 5))
