from collections import deque

N = int(input())

for n in range(N):
    
    vps = list(input())
    lst = []
    i = 0
    for i in range(len(vps)):
        
        if vps[i] == '(':
            lst.append(vps[i])
            
        else:
            if lst and lst[-1] == '(' :
                lst.pop()
                
            else:
                lst.append(vps[i])
    
    if lst:
        print('NO')
    else:
        print('YES')