def solution(s):
    tmp = s.split()
    c_tmp = []
    for number in tmp:
        c_tmp.append(int(number))

    c_tmp.sort()

    ans = ''
    ans += str(c_tmp[0]) + ' ' + str(c_tmp[-1])

    return ans


a = ['1 2 3 4', '-1 -2 -3 -4', '-1 -1']
for i in range(3):
    print(solution(a[i]))
