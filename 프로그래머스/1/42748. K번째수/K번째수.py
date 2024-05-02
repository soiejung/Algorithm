import heapq
def solution(array, commands):
    answer = []
    queue = []
    
    heapq.heapify(queue)
    for command in commands:
        start = command[0] - 1
        end = command[1] - 1
        idx = command[2] - 1
        lst = []
        for i in range(start,end+1):
            heapq.heappush(queue,array[i])
        
        for i in range(len(queue)):
            lst.append(heapq.heappop(queue))
            
        answer.append(lst[idx])
        queue = []
        
    return answer