M = int(input())
N = int(input())
# M = 60
# N = 100


def is_prime(n):
    if n == 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return 0
    return 1


min_prime = 0
sum_prime = 0

for number in range(M, N + 1):
    if is_prime(number):
        if not min_prime:
            min_prime = number
        sum_prime += number

if not sum_prime:
    print(-1)
else:
    print(sum_prime)
    print(min_prime)
