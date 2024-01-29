def gcd(a,b):
    
    if b > a:
        a, b = b, a
    
    while b != 0:
        n = a%b
        a = b
        b = n
    
    return a

def lcm(a,b):
    
    return int(a*b/gcd(a,b))

def solution(n, m):
    answer = []
    answer.append(gcd(n,m))
    answer.append(lcm(n,m))
    return answer