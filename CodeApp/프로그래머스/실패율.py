# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    result = []
    for i in range(1, N+1):
        total = 0
        fail = 0
        for s in stages:
            if s == i:
                fail += 1
                total += 1
            elif s > i:
                total += 1
        if total != 0:
            result.append([i,fail/total])
        else:
            result.append([i,0])
    
    result.sort(key=lambda x: (-x[1],x[0]))
    
    for r in result:
        answer.append(r[0])
    return answer