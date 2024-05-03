import itertools
def solution(k, dungeons):
    answer = 0
    
    idx = [i for i in range(len(dungeons))]
    
    for order in itertools.permutations(idx,len(idx)):
        now_k = k
        cnt = 0
        for index in order:
            if now_k >= dungeons[index][0]:
                now_k = now_k - dungeons[index][1]
                cnt += 1
            else:
                break
        
        if answer < cnt:
            answer = cnt

    return answer