from itertools import product


def find_floor(n):
    result = 1
    while True:
        if 2 ** result - 1 >= n:
            return result
        result += 1


def solution(numbers):
    answer = []

    for number in numbers:
        if number == 1:
            answer.append(1)
            continue

        b = bin(number)
        # print('2진법', b[2:])
        target = b[2:]
        len_bin = len(b[2:])
        floor = find_floor(len_bin)
        # print('floor', floor)

        while len(target) < 2 ** floor - 1:
            target = '0' + target
        print(target)

        flag = 0
        cnt = 0
        for i in range(len(target)):
            if i % 2:
                if target[i] == '0':
                    answer.append(0)
                    flag = 1
                    break
            else:
                if target[i] == '0':
                    cnt += 1

        if flag == 0:
            if cnt == len(target) // 2 + 1:
                answer.append(0)
            else:
                answer.append(1)

    return answer


print(solution([42]))
