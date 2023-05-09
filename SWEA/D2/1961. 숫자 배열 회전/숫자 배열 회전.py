def rotate(N,num):
    list_ = []
    M = []

    for p in range(num):
        for h in range(num-1, -1, -1):
            list_.append(N[h][p])
    for i in range(0,len(list_),num):
        list__ = list_[i:i+num]
        M.append(list__)
    return M

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    N = []
    temp1 = []
    temp2 = []
    N_1 = []
    N_2 = []
    N_3 = []
    for i in range(num):
        n = list(map(int, input().split()))
        N.append(n)
    
    N_1 = rotate(N,num)
    N_2 = rotate(N_1,num)
    N_3 = rotate(N_2, num)
    
    print(f'#{test_case}')
    for i in range(num):
        for j in range(num):
            print(N_1[i][j], end='')
        print(end=' ')
        for j in range(num):
            print(N_2[i][j],end='')     
        print(end=' ')
        for j in range(num):
            print(N_3[i][j],end='')
        print()
        
        

    