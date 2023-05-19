T = int(input())

for test_case in range(1,T+1):
    P = input().strip()
    Q = input().strip()
    flag = 1
    if P + 'a' == Q:
        flag = 0
    
    if flag:
        print(f'#{test_case} Y')
    else:    
        print(f'#{test_case} N')