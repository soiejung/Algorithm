import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# 최대공약수, 최소공배수
for i in range(min(a,b), 0, -1):
    
    if a%i == 0 and b % i == 0:
        print(i)
        # 최소공배수
        print(a*b//i)
        break
