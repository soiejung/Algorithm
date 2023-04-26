def solution(genres, plays):
    answer = []
    playsDic=[]
    gen_total = {}
    gen_total_s={}
    playsDic = [[genres[i], plays[i], i] for i in range(len(genres))]
    playsDic = sorted(playsDic, key=lambda x: (x[0],-x[1], x[2]))
    
    for g in playsDic:
        
        if g[0] in gen_total:
            
            gen_total[g[0]] += g[1]
        else:
            gen_total[g[0]] = g[1]
            
    gen_total_s = sorted(gen_total.items(), key=lambda x: -x[1])
    
    for g in gen_total_s:
        count = 0
        for p in playsDic:
            if g[0] == p[0]:
                count += 1
                if count > 2:
                    break
                else:
                    answer.append(p[2])

    return answer