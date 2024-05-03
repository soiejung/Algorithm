def solution(sizes):
    answer = 0
    w, h = 0,0
    
    for s in sizes:
        if s[0] > s[1]:
            if w < s[0]:
                w = s[0]
            if h < s[1]:
                h = s[1]
        else:
            if w < s[1]:
                w = s[1]
            if h < s[0]:
                h = s[0]
    

    answer = w * h
        
        
    return answer