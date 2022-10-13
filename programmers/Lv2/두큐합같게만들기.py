from collections import deque


def solution(queue1, queue2):
    q = []
    q.extend(queue1)
    q.extend(queue2)

    total = sum(q)
    if total % 2:
        return -1

    means = []
    # slicing해서 합이 total의 반이 되는 구간 찾기
    for i in range(len(q)):
        for j in range(i, len(q)):
            if sum(q[i: j + 1]) == total // 2:
                means.append((i, j))

    if not means:
        return -1

    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)

    for i in range(len(q1) * 3):
        if sum1 == sum2:
            return i

        if sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        else:
            num = q2.popleft()
            q1.append(num)
            sum1 += num
            sum2 -= num


print(solution([1, 10, 1, 2], [1, 2, 1, 2]))
