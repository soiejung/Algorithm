T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N, k = map(int, input().split())
    puzzle = []
    for i in range(N):
        n = list(map(int,input().split()))
        puzzle.append(n)
        
    count = 0
    for i in range(N):
        for j in range(N-k+1):
            length = 0
            for p in range(k):
                if puzzle[i][j+p] == 1:
                    length += 1
            if length == k:
                if j == 0:
                    if puzzle[i][j+k] == 0:
                        count+=1
                elif j == N-k:
                    if puzzle[i][j-1] == 0:
                        count += 1
                else:
                    if puzzle[i][j-1] == 0 and puzzle[i][j+k] == 0:
                        count += 1
                    
    for j in range(N):
        for i in range(N-k+1):
            length = 0
            for p in range(k):
                if puzzle[i+p][j] == 1:
                    length += 1
            if length == k:
                if i == 0:
                    if puzzle[i+k][j] == 0:
                        count += 1
                elif i == N-k:
                    if puzzle[i-1][j] == 0:
                        count += 1
                else:
                    if puzzle[i-1][j] == 0 and puzzle[i+k][j] == 0:
                        count += 1
    print(f'#{test_case} {count}')
        
                
                
        