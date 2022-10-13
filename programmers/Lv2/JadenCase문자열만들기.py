def solution(s):
    s_list = s.split()
    ans = []

    for i in range(len(s_list)):
        tmp = ''
        for j in range(len(s_list[i])):
            if j == 0:
                try:
                    tmp += s_list[i][j].upper()
                except ValueError:
                    tmp += s_list[i][j]
            else:
                try:
                    tmp += s_list[i][j].lower()
                except ValueError:
                    tmp += s_list[i][j]
        ans.append(tmp)

    result = ' '.join(map(str, ans))
    return result


print(solution("3people unFollowed me"))
