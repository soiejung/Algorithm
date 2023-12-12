# https://www.acmicpc.net/problem/1937

import sys
#sys.stdin = open("CodeApp/input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(99999999)
N = int(input())
trees = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)]for _ in range(N)]

# 모든 점을 방문한다!
# 방문한 뒤에 이동할 수 있는 모든 경우의 수를 재귀로 구현한다!
# 재귀로 구현한 뒤 DP로 바꾼다!

def recur(y,x):

    if dp[y][x] != 0:
        return dp[y][x]
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        ey = y + dy[i]
        ex = x + dx[i]

        if 0 <= ex < N and 0 <= ey < N:
            if trees[ey][ex] > trees[y][x]:
                dp[y][x] = max(dp[y][x],recur(ey,ex) + 1)

    return dp[y][x]        

for y in range(N):
    for x in range(N):
        recur(y,x)
        
print(max(map(max,dp))+1) # dp에서 max 값만 추출