import sys
sys.stdin = open("1002.txt", "r")

T = int(input())

for tc in range(T):
    info = list(map(int, input().split()))
    radius_sum = info[2] + info[5]
    center_gap = ((info[0] - info[3]) ** 2 + (info[1] - info[4]) ** 2) ** 0.5
    # print(center_gap)

    if center_gap > info[2] and center_gap > info[5]:
        # print('1번')
        if radius_sum < center_gap:
            print(0)
        elif radius_sum == center_gap:
            print(1)
        else:
            print(2)
    elif center_gap < info[2] and center_gap < info[5]:
        # print('2번')
        if info[0] == info[3] and info[1] == info[4]:
            if info[2] == info[5]:
                print(-1)
            else:
                print(0)
        else:
            print(2)
    elif center_gap > info[2] and center_gap < info[5]:
        # print('3번')
        if info[2] > info[5] - center_gap:
            print(2)
        elif info[2] == info[5] - center_gap:
            print(1)
        else:
            print(0)
    else:
        # print('4번')
        if info[5] > info[2] - center_gap:
            print(2)
        elif info[5] == info[2] - center_gap:
            print(1)
        else:
            print(0)
