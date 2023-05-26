def solution(maps):
    from collections import deque
    
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((0,0))
    dx = [ 0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    
    visited[0][0] = 1

    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx< n and 0<= ny< m and maps[nx][ny] == 1:
                
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    maps[nx][ny] = maps[x][y] + 1
        
                    
    if maps[n-1][m-1] == 1:
        
        return -1
    
    else:    
        
        return maps[n-1][m-1]