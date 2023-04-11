def solution(n, lost, reserve):
    answer = 0
    s = [1]*n
    
    for i in lost:
        s[i-1] -= 1
    for i in reserve:
        s[i-1] += 1
        
    for i in range(n):
        if s[i] == 0:
            if i != 0 and i != n-1:
                if s[i-1] == 2:
                    s[i-1] -= 1
                    s[i] += 1
                elif s[i+1] == 2:
                    s[i+1] -= 1
                    s[i] += 1
                    
            elif i==0:
                if s[i+1] == 2:
                    s[i+1] -= 1
                    s[i] += 1
            else:
                if s[i-1] == 2:
                    s[i-1] -= 1
                    s[i] += 1
    
    answer = n - s.count(0)
                    
                    
    return answer