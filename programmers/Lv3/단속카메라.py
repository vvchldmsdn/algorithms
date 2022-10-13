from itertools import combinations


def solution(routes):
    answer = 0

    routes = [[min(route), max(route)] for route in routes]
    total_min = 30000
    total_max = -30000
    for route in routes:
        s = route[0]
        e = route[1]
        total_max = max(total_max, s, e)
        total_min = min(total_min, s, e)

    return answer


print(solution([[-15, -20], [-14, -5], [-18, -13], [-5, -3]]))
