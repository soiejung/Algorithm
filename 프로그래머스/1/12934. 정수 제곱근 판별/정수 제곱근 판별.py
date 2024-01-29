def solution(n):
    answer = -1
    
    for i in range(1,int(n**(1/2))+1):
        if n == i**2:
            answer = (i+1)**2
            return answer
    
    return answer