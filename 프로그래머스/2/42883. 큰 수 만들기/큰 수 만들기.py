def solution(number, k):
    answer = ''
    select = len(number) - k
    
    idx = 0
    lst = []
    result = []
    for n in number:
        lst.append(int(n))
        
    while len(result) < len(number)-k:
        
        max_ = -1
        for i in range(idx, len(lst)-select+1):
            if max_ < lst[i]:
                max_ = lst[i]
                if max_ == 9:
                    break
        
        idx += lst[idx:len(lst)-select+1].index(max_) + 1
        #max_ = max(lst[idx:len(lst)-select+1])
        result.append(max_)
        #idx += lst[idx:len(lst)-select+1].index(max_) + 1
            
        select -= 1
    

    for r in result:
        answer += str(r)
    return answer