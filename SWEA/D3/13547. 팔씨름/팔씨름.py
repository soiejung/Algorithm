
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    lst = list(input())
    
    count = 0
  
    for l in lst:
        if l == 'o':
            count += 1
    flag = 0        
    if len(lst) < 15:
        if 15 - len(lst) >= 8-count:
            flag = 1
    elif len(lst) == 15:
        if count == 8:
            flag = 1
            
    if flag:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')