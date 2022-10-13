info = list(map(int, input().split()))
origin = [1, 1, 2, 2, 2, 8]

for i in range(len(info)):
    print(origin[i] - info[i], end=' ')
