def solution(n, stations, w):
    answer = 0

    last = 0
    cover = 2 * w + 1

    for station in stations:
        first = station - w
        if first > last:
            answer += (first - last - 1) // cover
            if (first - last - 1) % cover > 0:
                answer += 1
        last = station + w

    if last < n:
        answer += (n - last) // cover
        if (n - last) % cover > 0:
            answer += 1

    return answer


print(solution(11, [4, 11], 1))

# def solution(n, stations, w):
#     answer = 0

#     visited = [0] * (n + 1)

#     for station in stations:
#         for i in range(max(0, station - w), min(n + 1, station + w + 1)):
#             if visited[i] == 0:
#                 visited[i] = 1
#     print(visited)

#     cover = 2 * w + 1

#     i = 1
#     cnt = [0]
#     while i < len(visited):
#         if visited[i] == 0:
#             cnt[-1] += 1
#         else:
#             cnt.append(0)
#         i += 1

#     for num in cnt:
#         if num != 0:
#             answer += num // cover
#             if num % cover > 0:
#                 answer += 1
#     print(cnt)

#     return answer
