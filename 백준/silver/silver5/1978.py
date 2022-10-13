import sys
sys.stdin = open("1978.txt", "r")

N = int(input())
info = list(map(int, input().split()))


def prime_found(n):
    if n == 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return 0
    return 1


ans = 0

for i in range(len(info)):
    if prime_found(info[i]):
        ans += 1
print(ans)
