import re
def translate(n, k):
    
    lst = []
    result = ''
    while n > 1:
        a = n%k
        lst.append(a)
        n = int(n/k)
    
    if n != 0:
        lst.append(n)
    
    for i in range(len(lst)-1,-1,-1):
        result += str(lst[i])
        
    return result

def isPrime(n):

    if n == 1:
        return False
    
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    dp = []
    num = []
    result = translate(n,k)
    
    for cur in re.split('[0]',result):
        if not cur:
            continue
        else:
            num.append(int(cur))
    
    
    for n in num:
        
        if isPrime(n):
            answer += 1
        
    return answer