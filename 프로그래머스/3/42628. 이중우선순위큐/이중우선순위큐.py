import heapq
def solution(operations):
    answer = []
    queue = []

    for o in operations:

        do, num = o.split()
        num = int(num)
        if do == "I":
            heapq.heappush(queue,num)
            
        elif do == "D":
            if queue:
                if num == 1:
                    tmp1 = []
                    tmp2 = []
                    while queue:
                        if queue:
                            h = heapq.heappop(queue)
                            tmp1.append(-1*h)
                    for t in tmp1:
                        heapq.heappush(queue,t)
                    heapq.heappop(queue)
                    
                    while queue:
                        if queue:
                            h = heapq.heappop(queue)
                            tmp2.append(-1*h)
                    for t in tmp2:
                        heapq.heappush(queue,t)
                        
                elif num == -1:
                    heapq.heappop(queue)
    
    if not queue:
        min_, max_ = 0,0
    else:
        min_ = min(queue)
        max_ = max(queue)
    
    answer.append(max_)
    answer.append(min_)
    return answer