T = int(input())

lst = list(map(int, input().split()))

prefix = [0 for _ in range(T+1)]


# 이 전까지 더한 값이 그 다음 값보다 작은 경우엔 굳이 들고 갈 필요가 없다고 판단
for i in range(T):
    prefix[i+1] = max(prefix[i] + lst[i], lst[i])

prefix = prefix[1:] # 앞에 존재하는 0 제거
print(max(prefix))