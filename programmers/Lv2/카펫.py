def make_cases(n):
    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            result.append([n // i, i])

    return result


def solution(brown, yellow):
    total = brown + yellow

    cases = make_cases(total)
    for case in cases:
        if 2 * case[0] + 2 * case[1] - 4 == brown:
            return case
