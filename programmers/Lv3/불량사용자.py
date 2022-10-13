from itertools import permutations


def match(a, b):
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i] == '*':
            continue
        else:
            if a[i] != b[i]:
                return False

    return True


def solution(user_id, banned_id):
    answer = []

    for userinfo in permutations(user_id, len(banned_id)):

        cnt = 0
        for user, ban in zip(userinfo, banned_id):
            if match(ban, user):
                cnt += 1

        if cnt == len(banned_id):
            if set(userinfo) not in answer:
                answer.append(set(userinfo))

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
      ["fr*d*", "*rodo", "******", "******"]))
