def gcd(a,b):
    
    if b > a:
        a, b = b, a
    
    while b != 0:
        
        tmp = a % b
        a = b
        b = tmp
    
    return a
    

def solution(arrayA, arrayB):
    answer = 0
    a = 100000001
    b = 100000001
    n = len(arrayA)
    if n > 1:
        for i in range(n-1):
            a = min(a,gcd(arrayA[i],arrayA[i+1]))
            b = min(b,gcd(arrayB[i], arrayB[i+1]))
    else:
        a = arrayA[0]
        b = arrayB[0]
            
    
    if a == 1:
        a = 0
    if b == 1:
        b = 0
    
    
    # 철수가 가진 카드들을 모두 나눌 수 있고, 영희가 가진 카드를 모두 나눌 수 없는 경우
    if a != 0:
        flag1 = 1
        flag2 = 1
        for i in range(n):
            if arrayA[i] % a != 0:
                flag1 = 0
                break
        for i in range(n):
            if arrayB[i] % a == 0:
                flag2 = 0
                break
        
        if not flag1 or not flag2:
            a = 0
    
    # 철수가 가진 카드들을 모두 나눌 수 없고, 영희가 가진 카드를 모두 나눌 수 있는 경우
    if b != 0:
        flag1 = 1
        flag2 = 1

        for i in range(n):
            if arrayA[i] % b == 0:
                flag1 = 0
                break
        for i in range(n):
            if arrayB[i] % b != 0:
                flag2 = 0
                break
        
        if not flag1 or not flag2:
            b = 0
    
    if not a and not b:
        return 0
    
    answer = max(a,b)
    
    
    return answer