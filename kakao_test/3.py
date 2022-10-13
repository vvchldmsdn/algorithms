from itertools import product


def solution(users, emoticons):
    dis = [10, 20, 30, 40]
    data = product(dis, repeat=len(emoticons))

    t_plus = 0
    t_buy = 0
    for discount in data:  # 할인율 종류마다 하나씩 보자 (10,10)
        print('dicount', discount)
        plus = 0
        total_buy = 0
        for user in users:  # [40,10000]
            print('user', user)
            buy = 0
            for i in range(len(discount)):
                if discount[i] >= user[0]:  # 할인율 만족하면
                    buy += emoticons[i] * (100 - discount[i]) / 100
            print('buy', buy)
            if buy > user[1]:
                buy = 0
                plus += 1
            else:
                total_buy += buy
        if plus > t_plus:
            t_plus = plus
            t_buy = total_buy
        elif plus == t_plus:
            if t_buy < total_buy:
                t_buy = total_buy

    answer = [t_plus, t_buy]
    return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
