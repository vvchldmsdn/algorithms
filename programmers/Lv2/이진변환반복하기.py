def solution(s):
    cnt = 0
    zero_cnt = 0
    while s != '1':
        tmp = 0
        for byte in str(s):
            if byte == '1':
                tmp += 1
            else:
                zero_cnt += 1
        print(tmp)
        s = str(bin(tmp)[2:])
        print(s)
        cnt += 1
    return [cnt, zero_cnt]


print(solution("1111111"))
