T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    puzzle = []
    for i in range(9):
        n = list(map(int, input().split()))
        puzzle.append(n)
    
    flag = 1
    for i in range(9):
        check_r = [0]*9
        for j in range(9):
            for p in range(1,10):
                if puzzle[i][j] == p:
                    check_r[p-1] += 1
        for c in check_r:
            if c != 1:
                flag = 0
    
    for i in range(9):
        check_c = [0]*9
        for j in range(9):
            for p in range(1, 10):
                if puzzle[j][i] == p:
                    check_c[p-1] += 1
        for c in check_c:
            if c != 1:
                flag = 0
    
    for i in range(0,9,3):
        for j in range(0,9, 3):
            check_p = [0]*9
            for p in range(i,i+3):
                for h in range(j,j+3):
                    for l in range(1,10):
                    	if puzzle[p][h] == l:
                            check_p[l-1] += 1
            for c in check_p:
                if c != 1:
                    flag = 0
    
    if flag == 1:
        print(f'#{test_case} {flag}')
    else:
        print(f'#{test_case} {flag}')
    
                
    
