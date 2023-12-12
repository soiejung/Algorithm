import sys
#sys.stdin = open("복습/input.txt","r")

def gcd(x,y):

    while x%y != 0:
        tmp = x%y
        x = y
        y = tmp

    return y

N = int(input())

A = list(map(int, input().split()))
A.sort()
answer = 0
for i in range(N-1):
    if gcd(A[i],A[i+1]) != 1:
        for j in range(A[i]+1, A[i+1]):
            if gcd(A[i],j) == 1 and gcd(A[i+1],j) == 1:
                answer += 1
                break
            if j == A[i+1]-1:
                answer += 2

print(answer)