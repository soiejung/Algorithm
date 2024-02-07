def solution(n,a,b):
    answer = 1
    
    while True:
        
        if (a%2 == 0 and b == a-1) or (b%2 == 0 and a == b-1):
            break
        else:
            if a%2 == 0:
                a //= 2
            else:
                a += 1
                a //= 2
                
            if b%2 == 0:
                b //= 2
            else:
                b += 1
                b //= 2
            answer += 1
        
        
    return answer