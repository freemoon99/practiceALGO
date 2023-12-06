def solution(s):
    answer = True
    temp = []
    
    for c in s:
        if c == '(':
            temp.append(c)
        elif c == ')':
            if temp and temp[-1] == '(':
                temp.pop()
            else:
                temp.append(c)

    if temp:
        return False
    return True