def cal_time(a):
    result = 0

    for i in range(len(a) // 2):
        out_min = int(a[2 * i + 1][-2:])
        in_min = int(a[2 * i][-2:])
        out_hour = int(a[2 * i + 1][:2])
        in_hour = int(a[2 * i][:2])

        if out_min - in_min < 0:
            result += 60 + (out_min - in_min) + (out_hour - in_hour - 1) * 60
        else:
            result += (out_min - in_min) + (out_hour - in_hour) * 60

    return result


def solution(fees, records):
    cars = dict()

    for info in records:
        info = info.split()

        if int(info[1]) not in cars:
            cars[int(info[1])] = []

        cars[int(info[1])].append(info[0])

    ans = []
    for car in cars:
        if len(cars[car]) % 2:
            cars[car].append('23:59')
        total_time = cal_time(cars[car])

        total_fee = 0
        exceed = max(total_time - fees[0], 0)
        if exceed == 0:
            total_fee += fees[1]
        else:
            total_fee += fees[1] + (((exceed - 1) // fees[2]) + 1) * fees[3]

        ans.append((car, total_fee))

    ans.sort(key=lambda x: x[0])

    result = []
    for i in range(len(ans)):
        result.append(ans[i][1])

    return result


print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN",
      "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
