def solution(participant, completion):
    answer = ''
    dic = {}
    
    for p in participant:
        dic[p] = 0
    
    for p in participant:
        dic[p] += 1
    
    for c in completion:
        dic[c] -= 1
        

    for key,value in dic.items():
        if value > 0:
            answer += key
        
    return answer