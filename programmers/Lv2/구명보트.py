# def solution(people, limit):
#     light = min(people)
#     answer = 0
#     new = []

#     for i in range(len(people)):
#         if people[i] > limit - light:
#             answer += 1
#         else:
#             new.append(people[i])
#     # print(answer)
#     new.sort()
#     # print(new)
#     visited = []

#     for i in range(len(new) - 1, -1, -1):
#         if i not in visited:
#             curr = new[i]
#             for j in range(i - 1, -1, -1):
#                 if j not in visited:
#                     if curr + new[j] <= limit:
#                         visited.extend([i, j])
#                         answer += 1
#                         break

#     print(answer)
#     print(visited)
#     answer += len(new) - len(visited)

#     return answer


def solution(people, limit):
    people.sort()
    result = 0

    i = 0
    j = len(people) - 1

    while i <= j:
        result += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1

    return result


print(solution([7, 5, 8], 10))
