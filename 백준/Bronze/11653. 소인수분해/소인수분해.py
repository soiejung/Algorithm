import sys
input = sys.stdin.readline
N = int(input())
i=2
while True:
    
    if N % i == 0:
        print(i)
        N = N//i

    else:
        i+=1

    if N==1:
        break
