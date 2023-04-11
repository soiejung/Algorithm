def solution(n, computers):
    answer = 0
    visited = [False] * n

    

    def dfs(v):
        visited[v] = True
    
        for i in range(n):
            if not visited[i] and computers[v][i]:
                dfs(i)
            
    for idx in range(n):
        if not visited[idx]:
            dfs(idx)
            answer += 1
    return answer