from collections import deque
def solution(maps):
    answer = []
    matrix = []
    for m in maps:
        lst = []
        for mm in m:
            if mm == 'X':
                lst.append(0)
            else:
                lst.append(int(mm))
                
        matrix.append(lst)

    n = len(matrix)
    m = len(matrix[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x,y):
        
        queue = deque()
        queue.append([x,y])
        visited[x][y] = 1
        total = matrix[x][y]
        
        while queue:
            
            if queue:
                nx, ny = queue.popleft()
                
                for i in range(4):
                    
                    xx = nx + dx[i]
                    yy = ny + dy[i]
                    
                    if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy] and matrix[xx][yy]:
                        visited[xx][yy] = 1
                        total += matrix[xx][yy]
                        queue.append([xx,yy])
        
        return total
    
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] and not visited[i][j]:
                answer.append(bfs(i,j))
                    
    if not answer:
        return [-1]
    
    answer.sort()
    return answer