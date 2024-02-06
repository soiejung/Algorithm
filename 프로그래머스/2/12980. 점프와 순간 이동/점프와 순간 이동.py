def solution(n):
    ans = 0
    
    # n이 0이 될 때 까지
    while n > 0:
        
        # n이 짝수라면 배터리를 소모하지 않음
        if n % 2 == 0:
            n = n//2
    
        # n이 홀수면 배터리를 1 소모함 (짝수가 되려면 1 빼줘야해서)
        else:
            ans += 1
            n -=1
            n = n//2
    
    return ans