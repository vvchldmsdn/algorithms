def solution(n, words):
    answer = []

    visited = []
    for i in range(len(words)):
        if words[i] not in visited:
            if i != 0:
                if words[i][0] != visited[-1][-1]:
                    return [i % n + 1, i // n + 1]
                else:
                    visited.append(words[i])
            else:
                visited.append(words[i])
        else:
            return [i % n + 1, i // n + 1]

    return [0, 0]
