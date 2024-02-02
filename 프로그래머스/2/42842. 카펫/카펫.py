def solution(brown, yellow):
    answer = []
    
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            h = i
            w = yellow // i
            if brown + yellow == (h+2)*(w+2):
                answer.append(h+2)
                answer.append(w+2)
                
    
    answer.sort(reverse=True)
    return answer