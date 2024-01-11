def solution(s):
    answer = 0

    idx = 0
    
    while idx < len(s):
        
        if idx == len(s)-1:
            answer += 1
            return answer
        
        first = s[idx]
        same = 1    
        diff = 0
        for i in range(idx+1,len(s)):

            if first != s[i]:
                diff += 1
            else:
                same += 1

            if same != 0 and diff != 0 and same == diff:
                idx = i+1
                answer += 1
                break
                
            if same != diff and i == len(s)-1:
                answer += 1
                return answer
                
    return answer