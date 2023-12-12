import sys
#sys.stdin = open("복습/input.txt","r")

H, W = map(int, input().split())

block = list(map(int,input().split()))

total = 0

# 가장 높은 길이와 index 찾기
max_ = max(block)
max_idx = block.index(max_)

# 막대 길이의 합을 누적합으로 구하기
for i in range(len(block)):
    total += block[i]

# 누적합에서 최대 길이 빼주기
total -= max_
answer = 0

i = 0
j = 0
# 처음 시작부터 최대 길이의 index까지 구해주기
while j < max_idx:

    if block[i] >= block[j]:
        answer += block[i]
        j+=1
    else:
        i = j
        j = i

p = W-1
k = W-1
# 맨 끝 부터 최대 길이의 index 까지 구해주기
while k > max_idx:
    
    if block[p] >= block[k]:
        answer += block[p]
        k -= 1
    else:
        p = k
        k = p
    
# 전체 구한 부피에서 막대 부피만큼 빼주기
answer -= total
print(answer)