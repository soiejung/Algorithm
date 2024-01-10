# https://www.acmicpc.net/problem/2565

import sys

#sys.stdin = open("CodeApp/input.txt","r")
input = sys.stdin.readline

N = int(input())


lines = {}
dp = [1 for _ in range(N)]
line = [list(map(int,input().split()))for _ in range(N)]

# 순서대로 정렬
line = sorted(line, key=lambda x:x[0])


# A가 작은데 B가 큰 경우 교차된다.
# A를 기준으로 정렬한 B의 값을 비교하여 가장 긴 증가하는 부분 수열(LIS)를 구한다
# 답은 N - (최대 전깃줄의 수)
for i in range(N):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))