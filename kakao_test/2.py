def solution(cap, n, deliveries, pickups):
    answer = 0
    while sum(deliveries) + sum(pickups) > 0:
        # print('here')
        d_idx = p_idx = 0
        for i in range(n-1, -1, -1):
            if deliveries[i] != 0:
                d_idx = i
                break
        for i in range(n-1, -1, -1):
            if pickups[i] != 0:
                p_idx = i
                break

        m_idx = max(d_idx, p_idx)
        answer += (max(d_idx, p_idx) + 1) * 2

        db = pb = 0
        for i in range(m_idx, -1, -1):
            if deliveries[i] <= cap-db:
                db += deliveries[i]
                deliveries[i] = 0

        for i in range(m_idx, -1, -1):
            if pickups[i] <= cap-pb:
                pb += pickups[i]
                pickups[i] = 0

        # print(deliveries)
        # print(pickups)

    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
