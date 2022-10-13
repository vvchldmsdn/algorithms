from itertools import combinations_with_replacement


def solution(n, info):
    info.reverse()

    data = combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n)

    diff = 0
    result = []

    for combi in data:
        apeech = 0
        lion = 0

        tmp = [0] * 11
        for i in range(11):
            tmp[i] = combi.count(i)

        for i in range(11):
            if not (tmp[i] == 0 and info[i] == 0):
                if tmp[i] > info[i]:
                    lion += i
                else:
                    apeech += i

        if lion - apeech > diff:
            diff = lion - apeech
            result = tmp

    if diff == 0:
        return [-1]
    else:
        result.reverse()
        return result


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
