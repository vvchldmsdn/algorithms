def compare(b, duration):
    y, m, d = b.split('.')
    y = int(y)
    m = int(m)
    d = int(d)

    m += duration

    if m % 12 == 0:
        y += m // 12 - 1
        m = 12
    else:
        y += m // 12
        m %= 12

    d -= 1
    if d == 0:
        d = 28
        m -= 1
        if m == 0:
            m = 12
            y -= 1

    return (y, m, d)


def solution(today, terms, privacies):
    ty, tm, td = today.split('.')
    ty = int(ty)
    tm = int(tm)
    td = int(td)
    term_graph = dict()
    for term in terms:
        a, b = term.split()
        term_graph[a] = int(b)

    answer = []
    for privacy in privacies:
        date, type = privacy.split()
        y, m, d = compare(date, term_graph[type])
        print(y, m, d)
        if y < ty:
            answer.append(privacies.index(privacy) + 1)
        elif y == ty:
            if m < tm:
                answer.append(privacies.index(privacy) + 1)
            elif m == tm:
                if d < td:
                    answer.append(privacies.index(privacy) + 1)

    return answer


print(solution('2022.05.19', ['A 6', 'B 12', 'C 3'], [
      '2021.05.02 A', '2021.07.01 B', '2022.02.19 C', "2022.02.20 C"]))

print(solution('2020.01.01', ['Z 3', 'D 5'], [
      '2019.01.01 D', '2019.11.15 Z', '2019.08.02 D', "2019.07.01 D", "2018.12.28 Z"]))
