T = int(input())

answer = []
for i in range(2, int(T**(1/2))+1):

    while T%i == 0:
        answer.append(i)
        T = T//i

if T != 1:
    answer.append(T)

print(len(answer))
print(*answer)
