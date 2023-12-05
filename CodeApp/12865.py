#https://www.acmicpc.net/problem/12865
import sys

#sys.stdin = open("CodeApp/input.txt","r")
input = sys.stdin.readline

# dp
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