def solution(citations):
    answer = 0
    size = len(citations)
    list = citations
    list.sort(reverse = True)
    for i in range(size):    
        
        if i+1 > list[i]:  
            return i
        
    return size