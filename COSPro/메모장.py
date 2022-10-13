def solution(K, words):
    result = 0
    tmp = 0

    for word in words:
        if tmp == 0:
            if len(word) < K:
                tmp += len(word)
            elif len(word) == K:
                result += 1
        elif tmp > 0:
            if tmp + len(word) + 1 < K:
                tmp += len(word) + 1
            elif tmp + len(word) + 1 == K:
                tmp = 0
                result += 1
            elif tmp + len(word) + 1 > K:
                tmp = len(word)
                result += 1
    return result
