#https://www.acmicpc.net/problem/14501

import sys
sys.setrecursionlimit(99999999)
#sys.stdin = open("CodeApp/input.txt","r")
input = sys.stdin.readline

# 재귀
"""def recur(idx,pay):

    global answer
    if idx > N-1:
        if idx > N:
            return
        answer = max(answer, pay)
        return

    # 일을 안했을 때
    recur(idx+1, pay)

    # 일을 했을 때
    recur(idx+T[idx],pay+P[idx])
    """

# 탑다운 dp
"""
def recur(idx):

    if idx > N:
        return -99999999
    
    if idx == N:
        return 0
    
    # 이미 저장되어 있다면 비교할 필요 없음
    if dp[idx] != -1:
        return dp[idx]
    # 일을 하거나 안하거나 가장 큰 값을 dp에 저장
    dp[idx] = max(recur(idx+T[idx])+P[idx], recur(idx+1))

    return dp[idx]

N = int(input())

T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [-1 for _ in range(N)]
answer = recur(0)
print(answer)
"""

N = int(input())
interview = [list(map(int, input().split())) for _ in range(N)]
# 바텀업 dp
dp = [0 for _ in range(N+1)]

# 역순으로 하라는 뜻
for idx in range(N)[::-1]:

    if idx + interview[idx][0] > N:
        dp[idx] = dp[idx+1]
    else:
        # 점화식
        dp[idx] = max(dp[idx+interview[idx][0]]+interview[idx][1], dp[idx+1])

print(max(dp))