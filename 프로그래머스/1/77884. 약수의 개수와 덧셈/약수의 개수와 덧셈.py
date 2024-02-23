def solution(left, right):
    answer = 0
    
    dp = [0 for _ in range(right+1)]
    dp[1] = 1
    
    for i in range(2, right + 1):
        for j in range(1, min(right//i,i)):
            dp[i*j] += 2
    
    for i in range(2, int(right ** (1/2))+1):
        dp[i*i] += 1
    
    print(dp)
    for i in range(left, right+1):
        if dp[i] %2 == 0:
            answer += i
        else:
            answer -= i
    return answer