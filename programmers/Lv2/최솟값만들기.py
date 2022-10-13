def solution(A, B):
    A.sort(reverse=True)
    B.sort()

    result = 0
    for i in range(len(A)):
        result += A[i] * B[i]

    return result


print(solution([1, 4, 2], [5, 4, 4]))
