from pprint import pprint
import sys
sys.stdin = open('11724.txt', 'r')


N, M = map(int, input().split())

graph = dict()
for i in range(N):
    graph[i + 1] = []

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(N + 1)]

ans = 0

for i in range(1, N + 1):
    if graph[i]:
        if not visited[i]:
            ans += 1
            stack = [i]
            visited[i] = 1
            while stack:
                print(stack)
                next = stack.pop()
                for i in range(len(graph[next])):
                    if not visited[graph[next][i]]:
                        stack.append(graph[next][i])
                        visited[graph[next][i]] = 1
                        print(visited)
print(ans)
