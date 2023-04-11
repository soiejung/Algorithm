def solution(numbers):
    import heapq
    answer = ''
    size = len(numbers)
    l = list(map(str,numbers))
    l.sort(key=lambda x: x*3, reverse = True)
    answer = str(int(''.join(l)))
    
        
    


    return answer