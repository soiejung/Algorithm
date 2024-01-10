# https://www.acmicpc.net/problem/2304

N = int(input())

lst = {}

max_H = 0
min_L = 1001
max_L = 0

for _ in range(N):
    
    L, H = map(int, input().split())
    lst[L] = H
    if H > max_H:
        max_H = H

    if min_L > L:
        min_L = L

    if max_L < L:
        max_L = L

answer = 0

# 위에서 부터 아래로 for문 동작
for i in range(max_H,0, -1):
    min_j = 1001
    max_j = 0
    for j in lst.keys():
        # 존재하는 막대의 길이가 현재 길이보다 크다면
        if lst[j] >= i:
            # 최소 x와 최대 x 구하기
            if min_j > j:
                min_j = j
            if max_j < j:
                max_j = j

    # 최소 x 에서 부터 최대 x 까지 갯수 세기
    answer += (max_j - min_j)+1        
        

print(answer)