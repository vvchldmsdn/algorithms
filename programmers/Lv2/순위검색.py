def solution(info, query):
    result = [0] * len(query)

    for i in range(len(query)):
        req = query[i].split(' and ')
        req = req[:3] + req[-1].split()
        score = int(req[-1])
        req = req[:4]
        # print(req, score)
        n_care = req.count('-')

        for j in range(len(info)):
            cand = info[j].split()
            cand_score = int(cand[-1])
            cand = cand[:4]

            if len(set(cand) & set(req)) == 4 - n_care:
                # print(i, j)
                if cand_score >= score:
                    result[i] += 1

    # print(result)

    return result


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))


'''
def solution(info, query):
    for i in range(len(info)):
        info[i] = info[i].split(' ')

    for i in range(len(query)):
        query[i] = query[i].split(' and ')

    for i in range(len(query)):
        tmp = query[i][3].split(' ')
        tmp2 = query[i][:3]
        query[i] =  tmp2 + tmp

    info_dict = dict()
    for i in range(len(info)):
        info_dict[i] = dict()

    for i in range(len(info)):
        info_dict[i]['language'] = info[i][0]
        info_dict[i]['part'] = info[i][1]
        info_dict[i]['career'] = info[i][2]
        info_dict[i]['food'] = info[i][3]
        info_dict[i]['score'] = int(info[i][4])

    ans = []
    for i in range(len(query)):
        cnt = 0
        l = query[i][0]
        p = query[i][1]
        c = query[i][2]
        f = query[i][3]
        s = int(query[i][4])
        # print(i, l, p, c, f, s)
        for j in info_dict:
            tmp_cnt = 0

            if l != '-':
                if l == info_dict[j]['language']:
                    tmp_cnt += 1
            else:
                tmp_cnt += 1

            if p != '-':
                if p == info_dict[j]['part']:
                    tmp_cnt += 1
            else:
                tmp_cnt += 1

            if c != '-':
                if c == info_dict[j]['career']:
                    tmp_cnt += 1
            else:
                tmp_cnt += 1

            if f != '-':
                if f == info_dict[j]['food']:
                    tmp_cnt += 1
            else:
                tmp_cnt += 1

            if s <= info_dict[j]['score']:
                tmp_cnt += 1
            # print(f'i = {i} / j = {j} / tmp_cnt = {tmp_cnt}')
            if tmp_cnt == 5:
                cnt += 1
        ans.append(cnt)
    return ans
'''
