
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N, D = map(int,input().split())
    
    if (N)%(2*D+1) != 0:
        min_= (N)//(2*D+1) + 1
    else:
        min_ = (N)//(2*D+1) 
        
    print(f'#{test_case} {min_}')
