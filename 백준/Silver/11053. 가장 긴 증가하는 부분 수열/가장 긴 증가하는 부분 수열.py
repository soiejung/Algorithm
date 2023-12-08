# https://www.acmicpc.net/problem/11053

import sys

#sys.stdin = open("CodeApp/input.txt","r")
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))