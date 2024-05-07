from collections import deque
def solution(m, n, puddles):
    answer = 0
    
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]


    for i in range(1,n+1):
        for j in range(1,m+1):
            matrix[i][j] = 1

    for p in puddles:
        a, b = p[1], p[0]
        matrix[a][b] = 0
        if a == 1:
            for i in range(b+1,m+1):
                matrix[a][i] = 0
        if b == 1:
            for i in range(a+1,n+1):
                matrix[i][b] = 0
        
    for i in range(2,n+1):
        for j in range(2,m+1):
            if matrix[i][j] != 0:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    

    answer = matrix[n][m]
    if answer < 0:
        return 0
    return answer%1000000007

