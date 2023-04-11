def solution(operations):
    answer = []
    q = []
    import heapq

    for i in operations:
        if i[0] == 'I':
            heapq.heappush(q, int(i[2: ]))
        elif i == 'D -1':
            if q:
                heapq.heappop(q)
        else:
            if q:
                q.pop()
            
    if not q:
        answer = [0,0]
    else:
        answer = [max(q), min(q)]
            
    return answer