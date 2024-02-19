def solution(elements):
    answer = 0
    n = len(elements)
    dp = elements[:]
    lst = set(dp)

    for i in range(2,n+1):
        for j in range(n):
            dp[j] = dp[j] + elements[(i+j-1)%n]
            
            lst.add(dp[j]) 

    answer = len(lst)
    return answer
