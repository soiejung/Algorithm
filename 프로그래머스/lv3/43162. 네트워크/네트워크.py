def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    matrix = []
    
    for i in range(n):
        lst = []
        for j in range(n):
            if computers[i][j] == 1:
                lst.append(j)
        matrix.append(lst)

    
    def dfs(x):
        visited[x] = True
        for m in matrix[x]:
            if not visited[m]:
                dfs(m)
    
    for i in range(n):
        if not visited[i]:
            if not matrix[i]:
                answer += 1
                visited[i] = True
            else:
                dfs(i)
                answer += 1
    
    
    return answer

        
            