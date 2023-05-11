
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N = int(input())
    grid = []
    for i in range(N):
        lst = list(input())
        grid.append(lst)
        
    min_row = N-1
    max_row = 0
    min_col = N-1
    max_col = 0    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '#':
                if i < min_row:
                    min_row = i
                if i > max_row:
                    max_row = i
                if j < min_col:
                    min_col = j
                if j > max_col:
                    max_col = j
    flag = 1
    for i in range(min_row, max_row+1):
        for j in range(min_col, max_col + 1):
            if grid[i][j] != '#':
                flag = 0
                break
    if (max_col - min_col) != (max_row - min_row): 
        print(f'#{test_case} no')
    else:
        for i in range(min_row, max_row+1):
            for j in range(min_col, max_col + 1):
                if grid[i][j] != '#':
                    flag = 0
                    break
        if flag:
            print(f'#{test_case} yes')
        else:
            print(f'#{test_case} no')
                