#올바른 괄호
def solution(s):
    num = 0
    for i in s:
        if i == '(':
            num += 1
        else :
            if num:
                num -= 1
            else:
                return False
    if num:
        return False
    else:
        return True