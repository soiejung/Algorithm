import sys
input = sys.stdin.readline
M, N = map(int,input().split())
lst = [i for i in range(N+1)]

for i in range(2,N+1):
    
    if lst[i] == 0:
        continue
    
    for j in range(2*i, N+1,i):
        lst[j] = 0

lst[0] = 0
lst[1] = 0

for i in range(M, N+1):
    if lst[i] != 0:
        print(lst[i])
