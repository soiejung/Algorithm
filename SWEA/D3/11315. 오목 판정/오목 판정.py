
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    lst = []
    matrix=[]
    for i in range(N):
        lst = list(input())
        matrix.append(lst)
    
    
    dr = [0, 1, 1, 1]
    dc = [1, 1, 0, -1]
    flag = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'o':
                for d in range(4):
                    r = i
                    c = j
                    count = 0
                    while 0<= r <= N-1 and 0<= c<= N-1 and matrix[r][c] == 'o':
                        count += 1
                        r += dr[d]
                        c += dc[d]
                    if count >= 5:
                        flag = 1

    
    if flag :
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')
                    
