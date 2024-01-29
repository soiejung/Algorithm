def solution(n):
    answer = []
    
    str_n = str(n)
    
    for i in reversed(str_n):
        answer.append(int(i))
        
    return answer