T = int(input())
lst = list(map(int, input().split()))

answer = 0
for l in lst:
    flag = 1
    for i in range(2, int(l**0.5)+1):
        if l%i == 0:
            flag = 0

    if flag and l != 1:
        answer += 1


print(answer)