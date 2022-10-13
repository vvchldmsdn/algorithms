def solution(n, s):
    eq = 1
    if eq * n > s:
        return [-1]

    while eq * n <= s:
        eq += 1
    eq -= 1

    answer = [eq] * n
    diff = s - eq * n
    for i in range(n - 1, n - 1 - diff, -1):
        answer[i] += 1

    return answer


print(solution(2, 9))
