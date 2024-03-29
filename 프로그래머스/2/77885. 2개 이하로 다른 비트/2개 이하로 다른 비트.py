def binary(num):
    
    result = []

    while num > 1:
        
        a = num % 2
        result.append(a)
        num = int(num/2)
        
    if num > 0:
        result.append(num)
        
    result.reverse()
    
    return result
    
def solution(numbers):
    answer = []
    
    for n in numbers:
        
        # 짝수인 경우는 +1 인 숫자가 비트가 다른 지점이 2개 이하이면서 제일 작은 수
        # 짝수는 항상 비트의 끝이 0이기 때문에
        if n % 2 == 0:
            answer.append(n+1)
        
        # 홀수인 경우
        else:
            b1 = binary(n)
            b2 = binary(n+1)
            b = []
            if len(b2) != len(b1):
                b1 = [0] * (len(b2)-len(b1)) + b1
            
            
            for i in range(len(b1)-1,-1,-1):
                if b1[i] == 0:
                    idx = i
                    break
            
            for i in range(idx+2):
                b.append(b2[i])
            
            for i in range(idx+2,len(b1)):
                b.append(b1[i])
                
            num = 0
            for i in range(len(b)):
                num += b[i] * (2 ** (len(b1)-i-1))
            answer.append(num)

                    
    return answer