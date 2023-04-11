def solution(priorities, location):
    answer = 0
    index = []
    q = priorities
    queue = []

    for i in range(len(priorities)):
        index.append(i)

  
    while len(q)>0:
        
        max_p = max(q)   
        temp = q.pop(0)
        tmp =index.pop(0)
 
        if temp != max_p:
    
            q.append(temp)
            index.append(tmp)
        else:
            
            queue.append(tmp)
 
    answer = queue.index(location) +1
            

    return answer