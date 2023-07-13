def solution(park, routes):
    answer = []
    matrix = []

    for p in park:  
        matrix.append(p)
    
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "S":
                x, y = i, j
                
    dx = [0, 0, 1, -1] # 동서남북
    dy = [1, -1, 0, 0]
    
    i = 0
    for r in routes:
        r1, r2 = r.split()
        r2 = int(r2)
        if r1 == "E":
            i = 0
        elif r1 == "W":
            i = 1
        elif r1 == "S":
            i = 2
        elif r1 == "N":
            i = 3
        
        xx , yy = x, y
        index = []
        flag = 1
        for _ in range(r2):
            
            xx = xx + dx[i]
            yy = yy+ dy[i]

            if xx>=n or xx<0 or yy>=m or yy<0:
                flag = 0
            else:
                if matrix[xx][yy] == "X":
                    flag = 0

        if flag:
            x = xx
            y = yy
            

    answer.append(x)
    answer.append(y)

    return answer