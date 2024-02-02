from collections import deque
def solution(s):
    answer = -1
    
    ss = deque()
    
    for i in range(len(s)):
        if not ss:
            ss.append(s[i])
        else:
            if ss[-1] == s[i]:
                ss.pop()
            else:
                ss.append(s[i])
    
    if not ss:
        answer = 1
    else:
        answer = 0
        
    return answer