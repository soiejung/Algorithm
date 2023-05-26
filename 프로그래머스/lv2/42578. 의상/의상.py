def solution(clothes):
    answer = 1
    dict = {}
    
    for c in clothes:
        key = c[1]
        value = c[0]
        lst = []
        if key in dict.keys():
            for v in dict[key]:
                lst.append(v)
            lst.append(value)
            dict[key] = lst
            
        else:
            lst.append(value)
            dict[key] = lst
            
            
    for d in dict.keys():
        answer *= len(dict[d]) + 1
    answer -=1
    
    return answer