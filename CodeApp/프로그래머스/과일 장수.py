# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    
    box = len(score) // m

    for b in range(box):
        lst = []
        for i in range(m*b,m*b+m,1):
            lst.append(score[i])
        min_ = min(lst)
        answer += min_ * m
            
    return answer