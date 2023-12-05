#https://www.acmicpc.net/problem/12865
import sys

#sys.stdin = open("CodeApp/input.txt","r")
input = sys.stdin.readline

# 탑다운 dp
"""
def recur(idx,w):

    if w > K:
        return -999999999
    if idx == N:
        return 0

    if dp[idx][w] != -1:
        return dp[idx][w]
    
    dp[idx][w] = max(recur(idx+1, w + items[idx][0])+items[idx][1], recur(idx+1,w))

    return dp[idx][w]

N, K = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(100_001)]for _ in range(N)]

answer = recur(0,0)
print(answer)
"""

# 바텀업 dp

N, K = map(int, input().split())

items = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    items[i] = list(map(int, input().split()))

dp = [[0] * (K+1) for _ in range(N+1)]

for idx in range(1,N+1): # 행: 물건의 갯수
    for w in range(1,K+1): # 열: 가방의 최대 용량

        # 혅ㅐ 물건의 무게가 가방의 최대 용량보다 크다면
        if items[idx][0] > w:
            # 뒤에서 진행하는거라 앞 인덱스로 가야함
            dp[idx][w] = dp[idx-1][w]
        else:
            # 현재 물건의 무게가 가방의 최대 용량 이하라면
            # 현재 물건을 안 넣는 경우, 현재 물건의 무게만큼 뻬고 현재 물건을 넣은 경우 중 큰 것
            dp[idx][w] = max(dp[idx-1][w-items[idx][0]]+items[idx][1],dp[idx-1][w])

print(dp[-1][-1])


# 재귀로 풀었을 때 시간 초과!
"""def recur(idx,weight,result):

    global answer

    if weight > K:
        return

    if idx > N-1:
        answer = max(answer,result)
        return
    
    # 배낭에 안넣었을 때
    recur(idx+1,weight,result)

    #배낭에 넣었을 때
    recur(idx+1,weight+W[idx], result+V[idx])

N, K = map(int, input().split())

W = []
V = []
for _ in range(N):

    w, v = map(int, input().split())
    W.append(w)
    V.append(v)


answer = 0
recur(0,0,0)
print(answer)
"""