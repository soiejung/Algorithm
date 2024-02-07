def gcd(a,b):
    
    if b > a:
        a, b = b, a
        
    while b != 0:
        
        tmp = a%b
        a = b
        b = tmp
    
    return a
 
def lcm(a, b):
    
    return a*b//gcd(a,b)

def solution(arr):
    answer = 0
    
    result = lcm(arr[0],arr[1])
    
    for i in range(2, len(arr)):
        result = lcm(result,arr[i])
    
    answer = result
    return answer