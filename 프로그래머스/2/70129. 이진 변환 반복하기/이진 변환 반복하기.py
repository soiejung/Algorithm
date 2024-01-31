def binary(num):
    
    result = ''
    while num > 1:
        a = num%2
        num = num//2
        result += str(a)
    
    result += str(num)
    
    return ''.join(reversed(result))
        
    
    
def solution(s):
    answer = []
    cnt = 0
    count = 0
    while True:
        ss = ''
        for i in range(len(s)):
            if s[i] == '0':
                cnt += 1
            elif s[i] == '1':
                ss+=s[i]
        
        s = binary(len(ss))
        count += 1
        if s == '1':
            break
        
    answer = [count,cnt]
    
    return answer