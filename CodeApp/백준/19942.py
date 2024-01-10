# https://www.acmicpc.net/problem/19942

import sys
#sys.stdin = open("CodeApp/input.txt", "r")
input = sys.stdin.readline

def recur(idx, p, f, s, v, c):

    global answer
    global lst

    if idx == N:
        # 모든 영양소의 기준을 통과했다면
        if mp <= p and mf <= f and ms <= s and mv <= v:
            answer = min(answer,c)
            lst.append([answer,[a for a in arr]])
        return
    
    # 재료를 사용한 경우 영양소가 더해진다
    arr.append(idx+1)
    recur(idx+1, p+ingre[idx][0], f+ingre[idx][1], s+ingre[idx][2], v+ingre[idx][3], c+ingre[idx][4])
    arr.pop()
    # 재료를 사용하지 않은 경우 다음 재료로 넘어간다
    recur(idx+1, p, f, s, v, c)


N = int(input())
mp, mf, ms, mv = map(int, input().split())
ingre = [list(map(int, input().split())) for _ in range(N)]
answer = 999999999
arr = []
lst = []
recur(0,0,0,0,0,0)

lst.sort(key=lambda x: (x[0], x[1]))

if lst:
    print(lst[0][0])
    print(*lst[0][1])

else:
    print(-1)
