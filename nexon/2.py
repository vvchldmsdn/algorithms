def check(a, b):
    a_idx = 0
    b_idx = 0
    result = 0

    while result != len(b) and a_idx < len(a):
        if a[a_idx] == '_':
            a_idx += 1
        else:
            if a[a_idx] == b[b_idx]:
                result += 1
                a_idx += 1
                b_idx += 1
            else:
                a_idx += 1

    if result == len(b):
        return True
    else:
        return False


result = 0
order_idx = 0


def issubsequence(s1, s2):
    s2 = s2.replace('_', '')

    n, m = len(s1), len(s2)
    i, j = 0, 0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1

    # If i reaches end of s1,that mean we found all
    # characters of s1 in s2,
    # so s1 is subsequence of s2, else not
    return i == n


print(issubsequence('kd', 'hkbdi'))


def getMaximumRemovals(order, source, target):
    result = 0
    order_idx = 0

    while order_idx < len(order):
        source = source[:order[order_idx] - 1] + \
            '_' + source[order[order_idx]:]
        print(source)
        if issubsequence(target, source):
            # if check(source, target):
            print('통과')
            result += 1
            order_idx += 1
        else:
            return result
    return result


print(getMaximumRemovals([1, 4, 2, 3, 5], 'hkbdi', 'kd'))
