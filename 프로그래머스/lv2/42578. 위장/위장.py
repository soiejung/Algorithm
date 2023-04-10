def solution(clothes):
    answer = 0
    hashDict = {}
    row = len(clothes)
    for i in range(row):
        
        hashDict[clothes[i][0]] = clothes[i][1]
        
    count = {}
    sum = 1
    for i in hashDict.values():    
        if i in count:
            count[i] += 1        
        else:
            count[i] = 1
            
    for i in count:
        sum *= (count[i]+1)
    sum = sum-1
    answer = sum
    return answer