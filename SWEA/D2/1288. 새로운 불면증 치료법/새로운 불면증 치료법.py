
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = input()
    n = int(N)
    N_i = int(N)
    check = [0]*10
    count = 0
    c=0
    while c<10:
        for i in range(10):
            if check[i] != 1 and str(i) in N:
                check[i] = 1
                c+=1

        N_i += n
        N = str(N_i)
        count+=1

    print(f'#{test_case} {count*n}')
            
        
