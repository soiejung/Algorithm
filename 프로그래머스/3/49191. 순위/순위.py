def solution(n, results):
    answer = 0
    INF = 10**9
    dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(n+1):
            if i==j:
                dist[i][j] = 0

    # 자신이 이기는 경우
    for r in results:
        dist[r[0]][r[1]] = 1

    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    
    # 자신이 지는 경우
    for r in results:
        dist[r[1]][r[0]] = -1
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dist[i][k] < 0 and dist[k][j] < 0:
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    
    for i in range(1,n+1):
        flag = 1
        for j in range(1, n+1):
            if dist[i][j] == INF:
                flag = 0
                break
        if flag:
            answer += 1
    
    return answer