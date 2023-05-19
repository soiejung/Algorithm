
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N, p_d, p_g  = map(int,input().split())
    
    flag = 1
    if p_d != 0 and p_g == 0:
        flag = 0
    elif p_d != 100 and p_g == 100:
        flag = 0   
    else:
        for n in range(1, N+1):
            if (n * p_d) % 100 != 0:
                flag = 0
            else:
                flag = 1
                break
    
    if flag:
        print(f'#{test_case} Possible')
        
    else:
        print(f'#{test_case} Broken')
            
    