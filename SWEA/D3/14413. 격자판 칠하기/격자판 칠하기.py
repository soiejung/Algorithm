

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N, M = map(int,input().split())
    square = []
    for i in range(N):
        lst = list(input())
        square.append(lst)
    flag = 1
    board = [0] * 4
    for i in range(N):
        for j in range(M):
            if square[i][j] == '#':
                if (i+j) %2 == 0:
                    board[0] += 1
                else:
                    board[1] += 1
            elif square[i][j] == '.':
                if (i+j) %2 == 0:
                    board[2] += 1
                else:
                    board[3] += 1
    
    if (board[0] and board[1]) or (board[2] and board[3]) or (board[0] and board[2]) or (board[1] and board[3]):
        flag = 0
           
    if flag:
        print(f'#{test_case} possible')
    else:
        print(f'#{test_case} impossible')
                
                    
        
