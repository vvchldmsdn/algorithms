def make_todo(l, t):
    eq = 1
    while eq * l <= t:
        eq += 1
    eq -= 1

    todo = [eq] * l
    diff = t - eq * l
    for i in range(l - 1, l - 1 - diff, -1):
        todo[i] += 1

    return todo


def cal(n, works):
    if sum(works) <= n:
        return [0]

    works.sort()

    total_late = sum(works) - n
    todo = make_todo(len(works), total_late)

    flag = 0
    for i in range(len(works)):
        if todo[i] > works[i]:
            todo[i + 1] += todo[i] - works[i]
            todo[i] = works[i]
            todo.sort()
        else:
            flag = i
            break

    if flag != 0:
        return todo[:flag] + cal((sum(works[flag:]) - sum(todo[flag:])), works[flag:])
    else:
        return todo


def solution(n, works):
    tmp = cal(n, works)

    result = 0
    for i in range(len(tmp)):
        result += tmp[i] ** 2

    return result


print(solution(6, [1, 3, 3, 4, 15, 16]))
print(solution(3, [1, 1]))
