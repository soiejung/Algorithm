def solution(t, p):
    answer = 0
    
    for i in range(0,len(t)-len(p)+1):
        s = ''
        for j in range(i,i+len(p)):
            s += t[j]
        if s <= p:
            answer += 1
            
    return answer