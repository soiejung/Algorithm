# https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    answer = 0
    dp = [0 for _ in range(number+1)]
    dp[1] = 1
    for i in range(2, number+1):
        for j in range(1, min(number//i+1, i)):
            dp[i*j] += 2
            
    for i in range(2, int(number**(1/2))+1):
        dp[i**2] += 1
    
    for d in dp:
        if d > limit:
            answer += power
        else:
            answer += d
            
    return answer