def binary(n):
    
    count = 0
    result = []
    while n > 1:
        a = n%2
        result.append(a)
        n = n//2
        
    result.append(n)
    
    for r in result:
        if r == 1:
            count += 1
            
    return count
        
    
    
def solution(n):
    answer = 0
    
    cnt = binary(n)
    
    i = n+1
    while True:
        
        if binary(i) == cnt:
            answer = i
            break
        else:
            i += 1
        
    return answer