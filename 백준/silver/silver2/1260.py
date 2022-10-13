import sys
sys.stdin = open('1260.txt', 'r')

N, M, V = map(int, input().split())

graph = dict()
for i in range(N):
    graph[i + 1] = []

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for key in graph:
    graph[key].sort()

print(graph)

visited = [0] * (N + 1)

ans = []

for i in range(1, N + 1):
    if not visited[i]:
        visited[i] = 1
        stack = [i]
        while stack:
            next = stack.pop()
            ans.append(next)
            for i in range(len(graph[next]) - 1, -1, -1):
                if not visited[graph[next][i]]:
                    visited[graph[next][i]] = 1
                    stack.append(graph[next][i])
print(ans)
