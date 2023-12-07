# https://www.acmicpc.net/problem/11726

import sys
# 안넣으면 1000까지 반복이 끝나버려서 런타임 에러 발생
sys.setrecursionlimit(999999999)
#sys.stdin = open("CodeApp/input.txt","r")
input = sys.stdin.readline

N = int(input())
dp = [-1 for _ in range(N+1)]

dp[1] = 1

if N >= 2: # 안해주면 N=1일때 IndexError 발생
    dp[2] = 2

if N >= 3:
    for idx in range(3,N+1):
        dp[idx] = dp[idx-1] + dp[idx-2]

print(int(dp[-1]%10007))