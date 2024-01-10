A, B = map(int, input().split())

lst = list(map(int, input().split()))

prefix = [0 for _ in range(len(lst)+1)]



# 미리 누적합을 구해놓으면 한번만 계산하면 됨!
for i in range(A):
    prefix[i+1]= prefix[i] + lst[i]

answer = []
for i in range(B, A+1):
    answer.append(prefix[i]-prefix[i-B])

print(max(answer))