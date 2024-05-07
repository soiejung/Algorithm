import heapq
def solution(n, works):
    answer = 0
    
    hq = []
    
    for w in works:
        heapq.heappush(hq, -1 * w)
    
    for i in range(n):

        if hq[0] < 0:
            w = heapq.heappop(hq)
            w += 1
            heapq.heappush(hq,w)
        else:
            break

    for w in hq:
        answer += w**2
    
    
    return answer