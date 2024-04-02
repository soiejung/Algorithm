from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n+1)]
    maps = [[] for _ in range(n+1)]
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j:
                maps[i+1].append(j+1)

    

    def dfs(v):
        visited[v] = 1

        for i in maps[v]:
            if not visited[i]:
                dfs(i)
    
    for i in range(1,n+1):
        if not visited[i]:
            if not maps[i]:
                answer += 1
                visited[i] = 1
            else:
                dfs(i)
                answer += 1

            
    return answer