import sys
from collections import deque
sys.stdin = open('5430.txt', 'r')

T = int(input())

for tc in range(T):
    p = input()
    n = int(input())
    tmp_info = input()
    info = deque()

    for tmp in tmp_info:
        try:
            info.append(int(tmp))
        except ValueError:
            continue

    flag = 0
    for fun in p:
        if fun == 'R':
            info.rotate(-1)
        elif fun == 'D':
            if len(info) == 0:
                print('error')
                flag = 1
            else:
                info.popleft()

    if flag == 0:
        print(str(info))
