
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N = int(input())
    min_ = 2*N
    count = 0
    lst = []
    for i in range(1,int(N**(1/2))+1,1):
        if N % i == 0:
            lst.append(i)
            if N**(1/2) != N:
                lst.append(N//i)
    lst.sort()
 
    
    for l in lst:
        if l + (N//l) < min_:
            min_ = l + (N//l)
            count = l + (N//l) - 2
    print(f'#{test_case} {count}')
                    
                    
                    
