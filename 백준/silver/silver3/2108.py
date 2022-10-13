import math
import sys
sys.stdin = open('2108.txt', 'r')

N = int(input())
info = []

for _ in range(N):
    info.append(int(input()))

info.sort()

print(round(sum(info) / N))
print(info[N // 2])

dense = []
m_cnt = 0

for i in range(N):
    if info.count(info[i]) >= m_cnt:
        m_cnt = info.count(info[i])
        if info[i] not in dense:
            dense.append(info[i])
print(dense)
