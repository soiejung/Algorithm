def solution(want, number, discount):
    answer = 0
    dic = {}
    dd = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
        dd[want[i]] = 0
        
    for i in range(len(discount)-10+1):
        
        for j in range(i, i+10):
            if discount[j] in want:
                dd[discount[j]] += 1
        
        if dd == dic:
            answer += 1
        
        for i in range(len(want)):
            dd[want[i]] = 0
            
    return answer