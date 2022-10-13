dice = list(map(int, input().split()))

dice.sort()

if len(set(dice)) == 1:
    print(10000 + dice[0] * 1000)
elif len(set(dice)) == 2:
    if dice.count(dice[0]) == 2:
        print(1000 + dice[0] * 100)
    else:
        print(1000 + dice[2] * 100)
else:
    print(dice[2] * 100)
