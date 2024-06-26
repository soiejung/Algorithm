from collections import deque
def solution(maps):
    answer = 0
    INF = 1e9
    n = len(maps)
    m = len(maps[0])
    visited=[[0 for _ in range(m)] for _ in range(n)]
    dp = [[INF for _ in range(m)] for _ in range(n)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    x, y = 0, 0
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 1
    dp[x][y] = 1
    
    while queue:
        
        if queue:
            xx, yy = queue.popleft()
            for idx in range(4):
                nx = xx + dx[idx]
                ny = yy + dy[idx]

                if 0 <= nx < n and 0<= ny < m and not visited[nx][ny] and maps[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx,ny])
                    dp[nx][ny] = min(dp[nx][ny], dp[xx][yy]+1)
    
    if dp[-1][-1] == INF:
        return -1
    else:
        return dp[-1][-1]
