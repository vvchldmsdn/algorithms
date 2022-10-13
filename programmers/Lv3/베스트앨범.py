def solution(genres, plays):
    answer = []

    info = dict()
    for i in range(len(genres)):
        if genres[i] not in info:
            info[genres[i]] = [plays[i], [(i, plays[i])]]
        else:
            info[genres[i]][0] += plays[i]
            info[genres[i]][1].append((i, plays[i]))

    print(info)
    for genre in info:
        info[genre][1].sort(key=lambda x: x[1], reverse=True)
    print(info)

    sdict = sorted(info.items(), key=lambda x: x[1][0], reverse=True)
    print(sdict)

    for genre in sdict:
        if len(genre[1][1]) == 1:
            answer.append(genre[1][1][-1][0])
        else:
            for i in range(2):
                answer.append(genre[1][1][i][0])
    return answer


print(solution(["classic", "pop", "classic",
      "classic", "pop", "edm"], [500, 600, 150, 800, 2500, 1000]))
