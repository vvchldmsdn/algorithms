from collections import deque
import sys
sys.stdin = open('1966.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))
    # print('info = ', info)

    q = deque()
    q.extend(info)

    cnt = 0

    while q:
        if q[0] == max(q):
            if M == 0:
                cnt += 1
                print(cnt)
                break
            else:
                q.popleft()
                M -= 1
                cnt += 1
            # print('q = ', q, '/ M = ', M, '/ cnt = ', cnt)
        else:
            if M == 0:
                M = len(q) - 1
                q.rotate(-1)
            else:
                M -= 1
                q.rotate(-1)
            # print('q = ', q, '/ M = ', M, '/ cnt = ', cnt)

    # print('---------------------')
    # print('---------------------')
    # print('---------------------')
# q = deque()
# q.extend([0, 1, 2, 3, 4])

# q.rotate(-1)
# print(q)
