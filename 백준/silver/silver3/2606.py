import sys
sys.stdin = open('2606.txt', 'r')

N = int(input())

board = dict()
for i in range(1, N + 1):
    board[i] = []

num_node = int(input())
for i in range(num_node):
    tmp = list(map(int, input().split()))
    board[tmp[0]].append(tmp[1])
    board[tmp[1]].append(tmp[0])

visited = [False] * (N + 1)
visited[1] = True

stack = [1]
ans = 0

while stack:
    next = stack.pop()
    for edge in board[next]:
        if not visited[edge]:
            visited[edge] = True
            stack.append(edge)
            ans += 1

print(ans)
