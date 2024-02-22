def solution(cacheSize, cities):
    answer = 0
    miss, hit = 0,0
    
    if cacheSize > 0:
        cache = []

        idx = 0
        for c in cities:
            
            if c.lower() not in cache:
                miss += 1
                if len(cache) == cacheSize:
                    cache.pop(0)
                    cache.append(c.lower())
                else:
                    cache.append(c.lower())
            else:
                hit += 1
                cache.remove(c.lower())
                cache.append(c.lower())
                
        
        answer = miss * 5 + hit * 1
    else:
        answer = len(cities) * 5
        
    return answer