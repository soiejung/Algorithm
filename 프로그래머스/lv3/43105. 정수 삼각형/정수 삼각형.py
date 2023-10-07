def solution(triangle):
    answer = 0
    dp = [[0 for j in range(1,i+1)] for i in range(1,len(triangle)+1)]
    dp[0][0] = triangle[0][0]
    q = []
    x, y = 0,0
    q.append((0,0,triangle[0][0]))
    n = len(triangle)

    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])
    answer = max(dp[-1])
    return answer