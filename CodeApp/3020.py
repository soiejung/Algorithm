# https://www.acmicpc.net/problem/3020

import sys
input = sys.stdin.readline

# 이모스 법: 선의 시작을 1, 끝을 -1로 적은 후, 해당 칸의 값을 더한 수를 수열로 구한 후, 누적합을 진행하면 장애물이 몇개인지 알 수 있음

N, H = map(int, input().split())

lst = []

# 동굴을 가로에서 세로로 돌리겠음

lst = [0 for _ in range(H+1)]

for i in range(N):

    W = int(input())
    if i%2 == 0:
        lst[0] += 1
        lst[W] += -1
    else:
        lst[H] += -1
        lst[H-W] += 1

answer = [0 for _ in range(len(lst)+1)]
for i in range(len(lst)):
    answer[i+1] += answer[i] + lst[i]

_min = min(answer[1:-1])
count = answer[1:-1].count(_min)
print(_min, count)