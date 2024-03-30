def solution(n):
    answer = []
    
    # 아래, 오른쪽, 대각선 위
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    triangle = []
    total = 0
    for i in range(n):
        lst = []
        for j in range(i+1):
            lst.append(0)
            total += 1
        triangle.append(lst)
    
    print(total)
    x, y = 0,0
    idx = 0
    triangle[x][y] = 1
    for i in range(1,total):
        
        xx = x + dx[idx%3]
        yy = y + dy[idx%3]
        if 0 <= xx and  xx < len(triangle) and 0<= yy and yy < len(triangle[xx]):
            if triangle[xx][yy] == 0:
                x = x + dx[idx%3]
                y = y + dy[idx%3]
            else:
                idx += 1
                x = x + dx[idx%3]
                y = y + dy[idx%3]

        else:
            idx += 1
            x = x + dx[idx%3]
            y = y + dy[idx%3]
        
        triangle[x][y] = i+1
        
        
    
    for t in triangle:
        for tt in t:
            answer.append(tt)
        
            
        
            
    return answer