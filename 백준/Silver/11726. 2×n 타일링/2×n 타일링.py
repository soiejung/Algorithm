import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]
dp[1] = 1

if n >= 2:
    dp[2] = 2

if n >= 3:
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
        
print(int(dp[-1]%10007))

