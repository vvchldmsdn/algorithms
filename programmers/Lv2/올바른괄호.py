def solution(s):
    stack = []
    for paren in s:
        if paren == '(':
            stack.append('(')
        elif paren == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
        else:
            return False

    if stack:
        return False
    else:
        return True


print(solution("(())()"))
