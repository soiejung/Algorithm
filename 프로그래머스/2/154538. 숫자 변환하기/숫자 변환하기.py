from collections import deque
def solution(x, y, n):
    answer = 0
    
    def bfs(x,y,n):
        
        q = deque()
        # 방문 여부 확인 및 depth
        # 1로 해야 y로 변환가능 여부를 알 수 있음
        d[x] = 1
        q.append(x)
        
        while q:
            x = q.popleft()
            if 0 < x+n <= 1000000 and d[x+n] == 0:
                d[x+n] = d[x]+1
                q.append(x+n)
            if 0 < x * 2 <= 1000000 and d[x*2] == 0:
                d[x*2] = d[x]+1
                q.append(x*2)
            if 0 < x * 3 <= 1000000 and d[x*3] == 0:
                d[x*3] = d[x]+1
                q.append(x*3)
        
    d = [0] * 1000001
    bfs(x,y,n)

    return d[y]-1