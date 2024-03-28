def solution(topping):
    answer = 0
    

    
    a = [0 for _ in range(100001)]
    b = [0 for _ in range(100001)]
    
    # 과자 종류
    total = 0
    
    for t in topping:
        if b[t-1] == 0:
            total += 1
        b[t-1] += 1
    
    
    c1, c2 = 0, total
    
    for t in topping:

        if a[t-1] == 0:
            c1 += 1
        a[t-1] += 1
        
        if b[t-1] == 1:
            c2 -= 1
        b[t-1] -= 1
        
        if c1 == c2:
            answer += 1
    
    
    return answer