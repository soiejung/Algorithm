def solution(today, terms, privacies):
    answer = []
    year, month, date = map(int,today.split('.'))

    
    term_dic = {}
    for t in terms:
        key,value = t.split()
        term_dic[key] = int(value)

    
    for i in range(len(privacies)):
        p = privacies[i]
        start, type = p.split()
        y, m, d = map(int,start.split('.'))
        
        plus = int(term_dic[type]) * 28 -1
        plus_month = plus/28
        plus_date = plus%28
        
        m += int(plus_month)
        d += plus_date
        
        if m > 12:
            y1 = int(m/12)
            y += y1
            m = m%12
            
        if d > 28:
            m1 = int(d/28)
            d = d%28
            m += m1
            
        if m > 12:
            y1 = int(m/12)
            y += y1
            m = m%12

        if y < year:
            answer.append(i+1)
        elif y==year:
            if m < month:
                answer.append(i+1)
            elif m==month:
                if d < date:
                    answer.append(i+1)

                
    return answer