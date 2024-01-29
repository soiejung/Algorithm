def solution(s):
    answer = True
    isnum = ['1','2','3','4','5','6','7','8','9','0']
    flag = 1
    
    if len(s) != 4 and len(s) != 6:
        flag = 0
    
    for i in range(len(s)):
        if s[i] not in isnum:
            flag = 0
        
    if flag:
        return True
    else:
        return False