T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    n = []
    
    for i in range(N):
        n.append(list(map(int, input().split())))
    
    m = []
    
    for i in range(N+1-M):
        for k in range(N+1-M):
            sum_ = 0
            for j in range(M):
                for p in range(M):
                    sum_ += n[i+j][k+p] 
                  
            m.append(sum_)
         
    print(f'#{test_case} {max(m)}')
