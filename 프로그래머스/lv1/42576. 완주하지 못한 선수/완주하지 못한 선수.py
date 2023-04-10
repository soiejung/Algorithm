def solution(participant, completion):
    answer = ''
    hashDict = {}
    sum = 0
    
    for i in participant:
        hashDict[hash(i)] = i
        sum += hash(i)
    
    for i in completion:
        sum -= hash(i)
        
    answer = hashDict[sum]
    return answer