from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0]*n
    lst = []
    
    for i in range(n):
        l = []
        for j in range(n):
            if computers[i][j] == 1:
                l.append(j)
        lst.append(l)
                
    def dfs(v):
        
        visited[v] = 1
        for tmp in lst[v]:
            if not visited[tmp]:
                dfs(tmp)
                
    
    for i in range(n):
        if not visited[i]:
            if not lst[i]:
                answer += 1
                visited[i] = 1
            else:
                dfs(i)
                answer += 1
        
    return answer