import heapq
def solution(n, edge):
    answer = 0
    INF = 1e9
    matrix = [[] for _ in range(n+1)]
    distance = [INF for _ in range(n+1)]

    
    for i in range(len(edge)):
        matrix[edge[i][0]].append([edge[i][1],1])
        matrix[edge[i][1]].append([edge[i][0],1])


    #print(matrix)
    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q,(0,start))
        
        while q:
            if q:
                dist, now = heapq.heappop(q)
                
                if distance[now] < dist:
                    continue
                
                for n,l in matrix[now]:
                    length = dist + l
                    if length < distance[n]:
                        distance[n] = length
                        heapq.heappush(q,(length,n))
                        
        return max(distance[1:])
    
    max_ = dijkstra(1)
    answer = distance.count(max_)
    return answer