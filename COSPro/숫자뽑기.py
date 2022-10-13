def solution(arr, K):
    arr.sort()

    diff = []
    for i in range(len(arr) - 1):
        diff.append(arr[i + 1] - arr[i])

    result = max(arr)

    for i in range(len(arr) - K + 1):
        result = min(result, sum(diff[i: i + K - 1]))

    return result


print(solution([9, 11, 9, 6, 4, 19], 4))
