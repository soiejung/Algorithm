# https://school.programmers.co.kr/learn/courses/30/lessons/12921
def solution(n):
    answer = 0
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    
    for i in range(2, n+1):
        for j in range(1, min(n//i+1, i)):
            dp[i*j] += 2
    
    for i in range(2, int(n**(1/2))+1):
        dp[i**2] += 1
    
    for d in dp:
        if d == 2:
            answer += 1
    return answer