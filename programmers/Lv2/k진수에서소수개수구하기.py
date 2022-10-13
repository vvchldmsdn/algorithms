def base_change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    target = base_change(n, k)
    target = str(target)

    result = 0
    if '0' in target:
        target = target.split('0')
        for number in target:
            if number != '':
                if is_prime(int(number)):
                    result += 1
    else:
        if is_prime(int(target)):
            result += 1

    return result


print(solution(110011, 10))
