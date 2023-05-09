
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    n = int(input())
    N = [[0] * n for _ in range(n)]
    r, c = 0, 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    dist = 0
    for i in range(1,n*n+1):
        N[r][c] = i
        r += dr[dist]
        c += dc[dist]
        
        if r < 0 or c < 0 or r >= n or c >= n or N[r][c] != 0:
            r -= dr[dist]
            c -= dc[dist]
            dist = (dist+1)%4         
            r += dr[dist]
            c += dc[dist]
    
    print(f'#{test_case}')
    for row in N:
        print(*row)
        
            
                
            
        
