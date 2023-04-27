def solution(k, dungeons):
    from itertools import permutations
    answer = -1
    max = 0
    num = len(dungeons)
    n = []
    permu = []
    for i in range(num):
        n.append(i)
        
    permu += list(permutations(n,num))
    
    
    for p in permu:
        count = 0
        now_k = k
        for index in p:
                    
            if now_k >= dungeons[index][0]:
                now_k = now_k - dungeons[index][1]
                count += 1

        if max <= count:
            max = count
        
    answer = max
    return answer