def solution(d, budget):
    answer = 0
    
    d.sort()
    lst = []
    total = 0
    for i in range(len(d)):
        total += d[i]
        if total <= budget:
            lst.append(d[i])
    answer = len(lst)
    return answer