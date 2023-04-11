def solution(scoville, K):
    answer = 0
    import heapq
    heapq.heapify(scoville)        
    k = 0
    while scoville[0]<K:
        
        if len(scoville) >1:
            smallest = heapq.heappop(scoville)
            next_smallest = heapq.heappop(scoville)
            k = smallest + (next_smallest*2) 
            heapq.heappush(scoville,k)
            answer+=1
            
        else:
            answer = -1
            break

    return answer