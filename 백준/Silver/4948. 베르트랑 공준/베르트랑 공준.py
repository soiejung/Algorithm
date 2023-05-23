import sys
input = sys.stdin.readline

def isPrime(x):
    
    lst = [i for i in range(2*x+1)]
    lst[0] = 0
    lst[1] = 0
    count = 0
    for i in range(2, len(lst),1):
        
        if lst[i] == 0:
            continue
        
        for j in range(2*i, len(lst), i):
            lst[j] = 0
    
    for i in range(x+1, 2*x+1, 1):
        if lst[i] != 0:
            count += 1
    
    return count
    
while True:
    N = int(input())
    if N == 0:
        break
    
    else:
        print(isPrime(N))
       