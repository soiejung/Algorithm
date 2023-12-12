import sys
#sys.stdin = open("복습/input.txt","r")
sys.setrecursionlimit(99999999)
input = sys.stdin.readline

def recur(x, y):

    # 끝에 도달한 경우에 1을 세어줌
    if x == M-1 and y == N-1:
        return 1

    route = 0
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 재사용 해주는 코드 없으면 시간초과 남!!!!
    if dp[x][y] != -1:
        return dp[x][y]

    for i in range(4):
        ex = x + dx[i]
        ey = y + dy[i]

        if 0 <= ex < M and 0 <= ey < N:
            if graph[ex][ey] < graph[x][y]:
                # 재귀함수를 호출하면서 끝에 도달한 경우의 수를 세어줌
                route += recur(ex,ey)
    
    dp[x][y] = route
    return dp[x][y]

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

answer = recur(0,0)
print(answer)