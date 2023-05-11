from itertools import *
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = list(input())
    num = []
    for p in permutations(N,len(N)):
        temp = ''
        for i in p:
            temp+=i
        
        if temp[0] != '0':
            if int(temp) not in num:
                num.append(int(temp))
    
    flag = 0
    
    for i in range(1,len(num)):
        if num[i] % num[0] == 0:
            flag = 1
            break
            
    if flag:
            print(f'#{test_case} possible')
    else:
            print(f'#{test_case} impossible')
                     
