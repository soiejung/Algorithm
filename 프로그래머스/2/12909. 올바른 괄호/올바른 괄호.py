def solution(s):
    answer = True
    stack = []
    
    for ss in s:
        if not stack:
            stack.append(ss)
        else:
            if ss == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ss)
    
    if not stack:
        return True
    else:
        return False
