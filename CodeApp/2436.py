#https://www.acmicpc.net/problem/2436
#최소공배수 = A * B // 최대공약수
#최소공배수 * 최대공약수 = A * B
#최소공배수/최대공약수 = A' * B' (A'와 B'는 서로소)
# A' = A * 최대공약수
# B' = B * 최대공약수

A, B = map(int, input().split())

def _gcd(x,y):
    
    while x%y != 0:
        tmp = x%y
        x = y
        y = tmp
        
    return y

def _lcm(x,y):
    
    return x*y//_gcd(x,y)
    

tmp = int(B/A) #서로소들의 곱
resultA, resultB = -1, -1

for i in range(1, int((tmp)**(1/2))+1):
    if tmp % i == 0:
        a = i
        b = int(tmp/i)

        if _gcd(a,b) == 1: # 둘이 서로소 라는 뜻
            resultA = a * A
            resultB = b * A
            
print(resultA, resultB)