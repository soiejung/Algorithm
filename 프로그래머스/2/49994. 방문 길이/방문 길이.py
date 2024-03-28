def solution(dirs):
    answer = 0
    
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited = []
    idx = 0
    x , y = 0, 0
    
    visited.append([x,y,x,y])
    for i in range(len(dirs)):
        
        if dirs[i] == 'U':
            idx = 0
        elif dirs[i] == 'D':
            idx = 1
        elif dirs[i] == 'L':
            idx = 2
        else:
            idx = 3
        
        if x + dx[idx] >= -5 and x + dx[idx] <= 5 and y + dy[idx] >= -5 and y + dy[idx] <= 5:
            xx = x + dx[idx]
            yy = y + dy[idx]
            if [x,y,xx,yy] not in visited:
                if [xx,yy,x ,y] not in visited:
                    answer += 1
                visited.append([x,y,xx,yy])
                
            x = xx
            y = yy
        
        
        
        
    return answer