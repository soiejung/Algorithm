def solution(n, s):
    answer = []

    if s < n:
        return [-1]
    
    while s:
        
        a = int(s/n)
        answer.append(a)
        s -= a
        n -= 1
        
    return answer