from collections import deque
def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((0,0))
    n = len(maps)
    m = len(maps[0])

    while queue:    
        tmp1, tmp2 = queue.popleft()
        for i in range(4):
            x = dx[i] + tmp1
            y = dy[i] + tmp2    
            if 0 <= x < n and 0 <= y < m and maps[x][y] == 1:
                queue.append((x,y))
                maps[x][y] = maps[tmp1][tmp2] + 1
                
    if maps[n-1][m-1] > 1:
        answer = maps[n-1][m-1]
    else:
        answer = -1
    return answer