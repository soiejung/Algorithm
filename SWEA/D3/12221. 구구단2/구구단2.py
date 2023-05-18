
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    A,B = map(int,input().split())
    result = 0
    if A < 1 or A > 9 or B < 1 or B > 9:
        result = -1
    else:
        result = A * B
    print(f'#{test_case} {result}')
    
        
