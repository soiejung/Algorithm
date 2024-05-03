def solution(brown, yellow):
    answer = []
    
    for w in range(1,brown+yellow+1):
        for h in range(1,w+1):
            if w * h == brown + yellow and (w-2) * (h-2) == yellow:
                answer.append(w)
                answer.append(h)
                return answer
