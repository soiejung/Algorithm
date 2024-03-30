def solution(sequence, k):
    answer = [] 
    lst = []
    s = []
    
    for i in range(len(sequence)):
        if sequence[i] > k:
            break
        s.append(sequence[i])
        
    dp = [0] * (len(s)+1)
    for i in range(len(s)):      
        # 누적합
        dp[i+1] = dp[i] + s[i]
        
    #print(dp)
    for n in range(1,len(dp)):
        
        # 제일 큰 누적합에서 일정 간격의 누적합을 뺐을 때가 가장 큰 값
        # 그 큰 값이 k보다 작은 경우 해당 간격의 누적합들의 차가 모두 k보다 작다
        if dp[-1] - dp[-1-n] < k:
            continue
        
        last = len(dp)-1
        
        while last > n-1:
            #print(dp[last-n], dp[last])
            
            if dp[last] - dp[last-n] > k:
                last -= 1
            elif dp[last] - dp[last-n] == k:
                
                if s[last-n] != s[last-1]:
                    answer.append(last-n)
                    answer.append(last-1)
                else:
                    idx = s.index(s[last-1])
                    answer.append(idx)
                    answer.append(idx+n-1)
                    
                return answer
            else:
                break
