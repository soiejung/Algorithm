def solution(food):
    answer = ''
    result = []
    for i in range(1, len(food)):
        cnt = food[i] // 2
        if cnt > 0:
            for c in range(cnt):
                result.append(i)
    result.append(0)
    for i in range(len(result)-2,-1,-1):
        result.append(result[i])
    
    for r in result:
        answer += str(r)
            
    return answer