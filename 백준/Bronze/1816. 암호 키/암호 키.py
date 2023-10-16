T = int(input())

for t in range(T):
    
    N = int(input())
    flag = 1
    for i in range(2, 1000001):
        if N % i == 0:
            flag = 0
            break
    
    if flag:
        print("YES")
    
    else:
        print("NO")
    