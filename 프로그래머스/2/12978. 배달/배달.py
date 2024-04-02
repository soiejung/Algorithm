from collections import deque
import heapq

INF = 500001

def solution(N, road, K):
    answer = 0

    matrix = [[INF for _ in range(N+1)] for _ in range(N+1)]
    distance = [INF for _ in range(N+1)] 
    for i in range(len(road)):    
        a = road[i][0]
        b = road[i][1]
        c = road[i][2]
        matrix[a][b] = min(c,matrix[a][b])
        matrix[b][a] = min(c,matrix[b][a])
    
    def dijkstra(start):
    
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0
        
        while q:
            
            if q:
                dist, now = heapq.heappop(q)
                if distance[now] < dist:
                    continue
                
                for i in range(len(matrix[now])):
                    length = dist + matrix[now][i]
                    
                    if length < distance[i]:
                        distance[i] = length
                        heapq.heappush(q,(length,i))
    
    dijkstra(1)
    #print(distance)
    for i in range(1,len(distance)):
        if distance[i] <= K:
            answer += 1
    return answer