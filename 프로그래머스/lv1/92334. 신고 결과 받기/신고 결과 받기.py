def solution(id_list, report, k):
    answer = []
    
    dic = {}
    lst = {}
    result = {}
    
    for i in id_list:
        dic[i] = 0
        lst[i] = []
        result[i] = 0
        
        
    for l in report:
        id, r = l.split()
        if r not in lst[id]:
            lst[id].append(r)
            dic[r] = dic[r] + 1
    

    for key, value in lst.items(): 
        for v in value:
            
            if dic[v] >= k:
                result[key] += 1

    for value in result.values():
        answer.append(value)
        
    return answer