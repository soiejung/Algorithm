def solution(citations):
    answer = 0
    max_ = max(citations)
    num = 0
    
    while num <= max_:
        
        cnt1, cnt2 = 0, 0
        
        for c in citations:
            if c >= num:
                cnt1 += 1
            else:
                cnt2 += 1

        if num <= cnt1:
            if answer < num:
                answer = num
        
        num += 1
        
    return answer