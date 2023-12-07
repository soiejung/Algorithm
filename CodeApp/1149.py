# https://www.acmicpc.net/problem/1149

import sys

#sys.stdin = open("CodeApp/input.txt", "r")
input = sys.stdin.readline

N = int(input())

prices = [list(map(int, input().split()))for _ in range(N)]

dp = [[-1 for _ in range(3)] for _ in range(N)]
dp[0] = prices[0]

for idx in range(1,N):
    for RGB in range(3):
        
        if RGB == 0: # 빨간색을 칠할 경우
            # 자신 이전 집의 파란색, 초록색 중 최소 값을 더해준다
            dp[idx][RGB] = min(dp[idx-1][1], dp[idx-1][2]) + prices[idx][RGB]
        
        elif RGB == 1:
            dp[idx][RGB] = min(dp[idx-1][0], dp[idx-1][2]) + prices[idx][RGB]
        
        elif RGB == 2:
            dp[idx][RGB] = min(dp[idx-1][0], dp[idx-1][1]) + prices[idx][RGB]

print(min(dp[-1]))
