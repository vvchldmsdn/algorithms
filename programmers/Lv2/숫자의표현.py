def solution(n):
    answer = 1

    for i in range(1, n):
        tmp = i
        next = i + 1
        while tmp <= n:
            tmp += next
            next += 1
            if tmp == n:
                answer += 1
                break

    return answer


print(solution(15))
