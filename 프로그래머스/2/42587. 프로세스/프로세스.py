from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    lst = []
    for i in range(len(priorities)):
        queue.append([chr(65+i),priorities[i]])
    
    
    while queue:
        if queue:
            start, priority = queue.popleft()
            if queue:
                max_ = queue[0][1]
                for q in queue:
                    if max_< q[1]:
                        max_ = q[1]
                        
                if priority < max_:
                    queue.append([start,priority])
                else:
                    lst.append(start)
            else:
                lst.append(start)
    
    c = chr(65 + location)
    answer = lst.index(c) + 1

    return answer