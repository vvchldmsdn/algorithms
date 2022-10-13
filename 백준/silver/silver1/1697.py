import sys
from collections import deque
sys.stdin = open('1697.txt', 'r')

N, K = map(int, input().split())


def bound_check(x):
    return 0 <= x <= 100000


def bfs(n):
    q = deque()
    q.append(n)

    visited = [200000] * 100001
    visited[n] = 0
    while q:
        x = q.popleft()
        if x == K:
            return visited[x]
        for i in range(3):
            if i == 0:
                new_x = x - 1
            elif i == 1:
                new_x = x + 1
            else:
                new_x = 2 * x

            if bound_check(new_x) and visited[new_x] == 200000:
                visited[new_x] = visited[x] + 1
                q.append(new_x)


print(bfs(N))
