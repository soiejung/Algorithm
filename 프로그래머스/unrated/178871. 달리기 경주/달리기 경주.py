def solution(players, callings):
    answer = []
    p = {}
    r = {}
    for i in range(len(players)):
        p[players[i]] = i # players:rank
        r[i] = players[i] # rank:players
    
    
    for c in callings:
        rank = p[c]
        
        r[rank-1], r[rank] = r[rank], r[rank-1]
        p[r[rank-1]], p[r[rank]] = p[r[rank]], p[r[rank-1]]


    answer = list(r.values())
    return answer