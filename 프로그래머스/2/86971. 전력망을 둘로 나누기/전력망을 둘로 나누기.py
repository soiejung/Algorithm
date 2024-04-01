from collections import deque
def solution(n, wires):
    answer = 100
    
    matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]



    for i in range(len(wires)):
        matrix[wires[i][0]][wires[i][1]] = 1
        matrix[wires[i][1]][wires[i][0]] = 1

        
    def bfs(start,end,visited):
        
        queue = deque()
        queue.append(start)
        visited[start] = 1
        cnt = 1
        while queue:

            if queue:
                q = queue.popleft()
                
                for i in range(len(matrix[q])):                        
                    if i == end:
                            continue
                    if not visited[i] and matrix[q][i] == 1:
                        queue.append(i)
                        visited[i] = 1
                        cnt += 1
        return cnt
        
        
    for i in range(1,len(matrix)):
        for j in range(i,len(matrix[i])):
            visited = [0 for _ in range(n+1)]
            if matrix[i][j] == 1:
                a = bfs(i,j,visited)
                b = bfs(j,n+1,visited)
                answer = min(answer, abs(a-b))
        
    
    return answer