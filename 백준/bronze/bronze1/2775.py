T = int(input())

for t in range(T):
    k = int(input())  # 층
    n = int(input())  # 호

    building = [[0] * n for _ in range(k + 1)]

    for i in range(len(building[0])):
        building[0][i] = i + 1

    for i in range(1, k + 1):
        for j in range(n):
            building[i][j] = sum(building[i - 1][:j + 1])

    print(building[-1][-1])
