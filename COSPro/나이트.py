def solution(location):
    dx = [-2, -2, -1, 1, 2, 2, 1, -1]
    dy = [-1, 1, 2, 2, 1, -1, -2, -2]

    x = 0
    y = 0

    if location[0] == 'A':
        x = 0
    elif location[0] == 'B':
        x = 1
    elif location[0] == 'C':
        x = 2
    elif location[0] == 'D':
        x = 3
    elif location[0] == 'E':
        x = 4
    elif location[0] == 'F':
        x = 5
    elif location[0] == 'G':
        x = 6
    elif location[0] == 'H':
        x = 7

    y = int(location[1]) - 1

    result = 0
    for d in range(8):
        if 0 <= x + dx[d] < 8 and 0 <= y + dy[d] < 8:
            result += 1

    return result


print(solution('A7'))
