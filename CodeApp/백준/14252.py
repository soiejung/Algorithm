# https://www.acmicpc.net/problem/14252
# 두 수의 공약수가 1보다 큰 경우는 no
# 두 수의 공약수가 1인 경우만 ok
# 하나만 추가할지 두개를 추가할지 정하기
# 세개까지는 필요하지 않음 -> 귀납법으로 증명가능하다함

T = int(input())

lst = list(map(int, input().split()))

lst.sort()
def _gcd(x,y):
    
    while x%y != 0:
        tmp = x%y
        x = y
        y = tmp
        
    return y

answer = 0

for i in range(len(lst)-1):
    
    if _gcd(lst[i], lst[i+1]) != 1:
        # 두 수의 최대공약수가 1보다 큰 경우
        for j in range(lst[i], lst[i+1]):
            # 두 숫자 사이의 수들 중 하나의 숫자를 추가해서 양쪽다 최대 공약수가 1이 되는 경우
            
            if _gcd(lst[i], j) == 1:
                if _gcd(lst[i+1], j) == 1:
                    answer += 1
                    break
                
            # 끝까지 갔을 때 하나의 숫자로는 안될 때 두개의 숫자 추가 
            if j == lst[i+1]-1:
                answer += 2
            
    
print(answer)