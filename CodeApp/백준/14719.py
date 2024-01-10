# https://www.acmicpc.net/problem/14719

H, W = map(int, input().split())

lst = list(map(int,input().split()))

# 가장 높은 높이 구하기
max_H = max(lst)

check = 0 # 물이 고일 수 있는 환경인지 체크

count = 0
for l in lst:
    if l == 0:
        count += 1

# 기둥의 높이가 1 높은 것이 2개 이상이어야 물이 고일 수 있음
if len(lst) - count >= 2:
    check = 1

answer = 0
if check:
    block_weight = 0

    # 나중에 빼줄 블록 무게를 구한다
    for l in lst:
        block_weight += l


    # 블록을 쌓았을 때 빈 공간 생각하지 않고 덩어리채? 천을 올린것처럼 생각한다
    for i in range(max_H, 0, -1):
        max_w = 0
        min_w = W
        for j in range(len(lst)):
            if lst[j] >= i:
                if max_w < j:
                    max_w = j

                if min_w > j:
                    min_w = j            
        
        # 달라야 빗물이 고일 수 있음
        # 0부터 시작하므로 1 더해줘야 함
        answer += (max_w+1) - (min_w+1) + 1

    # 이전에 구해놓은 블록 자체의 크기를 빼주어 빗물이 고인 부피를 계산
    answer -= block_weight

print(answer)