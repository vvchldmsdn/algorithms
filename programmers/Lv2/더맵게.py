from heapq import heappop, heappush, heapify


def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while scoville[0] < K:
        first = heappop(scoville)
        if len(scoville) == 0:
            return -1
        second = heappop(scoville)

        new = first + 2 * second
        heappush(scoville, new)
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
