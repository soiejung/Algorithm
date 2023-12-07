# https://www.acmicpc.net/problem/1520

import sys
sys.setrecursionlimit(9999999)

#sys.stdin = open("Algorithm/CodeApp/input.txt", "r")

input = sys.stdin.readline


def recur(x,y):

    if x == M-1 and y == N-1:
        return 1 # 마지막까지 도달한 경우에 1 리턴

    # 상하좌우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    route = 0

    if dp[x][y] != -1: # 경로가 없는 경우에서도 재사용 방지를 위해 -1로 설정
        return dp[x][y]

    for i in range(4):
        ex = x+dx[i]
        ey = y+dy[i]

        if 0<= ex < M and 0 <= ey < N:

            if graph[ex][ey] < graph[x][y]:
                route += recur(ex,ey) # 끝까지 도달한 경우를 세어서 더해줌
        
    dp[x][y] = route
    return dp[x][y]




M, N = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(M)]

dp = [[-1 for _ in range(N)]for _ in range(M)]
answer = recur(0,0)
print(answer)