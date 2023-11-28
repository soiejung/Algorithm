# https://www.acmicpc.net/problem/2961
import sys
input = sys.stdin.readline

def recur(idx, sin, ssen, use):

    global answer

    if idx == N:
        if use == 0: # 아무 재료도 사용하지 않았다면
            return
        result = abs(sin-ssen)
        answer = min(answer, result)
        return

    # 사용한 경우    
    recur(idx+1, sin*ingre[idx][0], ssen+ingre[idx][1], use+1)
    
    # 사용하지 않은 경우
    recur(idx+1, sin, ssen, use)

N = int(input())

ingre = [list(map(int, input().split())) for _ in range(N)]
answer = 999999999999

recur(0,1,0,0)
print(answer)