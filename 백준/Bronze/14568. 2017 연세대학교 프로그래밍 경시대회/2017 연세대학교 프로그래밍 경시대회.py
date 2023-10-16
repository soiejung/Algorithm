
T = int(input())
answer = 0

for A in range(1, T+1):
    for B in range(1, T+1):
        for C in range(1, T+1):
                if A+B+C == T:
                    if A >= B+2:
                        if A and B and C:
                            if C%2 == 0:
                                answer += 1

print(answer)