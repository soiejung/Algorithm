

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    D, L, N = map(int, input().split())
    damage = 0
    for n in range(0,N):
        damage += D*(1+n*L*(1/100))
 
    
    print(f'#{test_case} {int(damage)}')