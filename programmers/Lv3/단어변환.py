def check(a, b):
    result = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1
    return result


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = list()

    stack = [(begin, 0)]
    while stack:
        next, cnt = stack.pop()
        if next == target:
            return cnt
        if next != begin:
            visited.append(next)
        for word in words:
            if word not in visited and check(next, word) <= 1:
                stack.append((word, cnt + 1))

    return 0


print()