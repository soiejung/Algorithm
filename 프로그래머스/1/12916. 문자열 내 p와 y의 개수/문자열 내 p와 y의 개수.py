def solution(s):
    answer = True
    
    cnt1, cnt2 = 0, 0
    
    for i in range(len(s)):
        if s[i] == 'P' or s[i] == 'p':
            cnt1 += 1
        elif s[i] == 'Y' or s[i] == 'y':
            cnt2 += 1
            
    if cnt1 == cnt2:
        return True
    else:
        return False