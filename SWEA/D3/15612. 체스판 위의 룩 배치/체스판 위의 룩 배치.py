
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    
    chess = [[ 0 for i in range(8)] for j in range(8)]
    count = 0
    for i in range(8):
        lst = list(input())
        for j in range(8):
            if lst[j] == 'O':
                chess[i][j] = 1
                count += 1
    
    if count != 8:
        print(f'#{test_case} no')
    else:
        flag = 1
        visit = [[ 0 for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                if visit[i][j] == 0  and chess[i][j] == 1:
                    for p in range(8):
                        visit[i][p] = 1
                        visit[p][j] = 1
                elif visit[i][j] == 1 and chess[i][j] == 1:
                    flag = 0
                    break
        if flag:
            print(f'#{test_case} yes')
        else:
            print(f'#{test_case} no')
                