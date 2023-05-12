
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    S = input()
    
    if S == 'MON':
        day = 6
    elif S == 'TUE':
        day = 5
    elif S == 'WED':
        day = 4
    elif S == 'THU':
        day = 3
    elif S == 'FRI':
        day = 2
    elif S == 'SAT':
        day = 1
    elif S == 'SUN':
        day = 7
        
    print(f'#{test_case} {day}')  
