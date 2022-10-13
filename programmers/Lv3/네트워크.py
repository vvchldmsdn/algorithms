def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(n):
        if not visited[i]:
            answer += 1
            stack = [i]
            while stack:
                next = stack.pop()
                visited[next] = 1
                for j in range(n):
                    if computers[next][j] == 1 and not visited[j]:
                        stack.append(j)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
