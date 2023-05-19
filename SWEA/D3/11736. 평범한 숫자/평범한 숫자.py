

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N = int(input())
    p = list(map(int, input().split()))
    
    count = 0
    for i in range(1,N-1):
        if p[i] < p[i+1] and p[i] > p[i-1]:
            count += 1
        elif p[i] > p[i+1] and p[i] < p[i-1]:
            count += 1
        
    print(f'#{test_case} {count}')