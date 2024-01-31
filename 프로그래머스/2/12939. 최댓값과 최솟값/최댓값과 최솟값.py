import re
def solution(s):
    answer = ''
    lst = []
    
    for cur in re.split("[ ]",s):
        if not cur:
            continue
        lst.append(int(cur))
    
    lst.sort()
    
    answer += str(lst[0])
    answer += ' '
    answer += str(lst[-1])
    return answer