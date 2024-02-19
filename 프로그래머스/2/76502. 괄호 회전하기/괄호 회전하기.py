def check(s):
    
    stack = []
    
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if (stack[-1] == '[' and s[i] == ']') or (stack[-1] == '{' and s[i] == '}') or (stack[-1] == '(' and s[i] == ')'):
                stack.pop()
            else:
                stack.append(s[i])
                
    if not stack:
        return 1
    else:
        return 0

def solution(s):
    answer = 0
    ss = s
    for i in range(len(s)):
        
        answer += check(ss)
        ss = ss[1:]+ss[0]
        
    
    
    return answer