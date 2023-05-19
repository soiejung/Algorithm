
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N = int(input())
    
    flag = 0
    for a in range(1,10):
        if N % a == 0:
            b = N // a
            if b >= 1 and b <= 9:
                flag = 1
                break
    
    if flag:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')
