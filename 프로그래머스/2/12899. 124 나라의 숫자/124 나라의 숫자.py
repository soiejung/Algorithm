from collections import deque
def func(n):
    
    lst = []
    
    while n > 0:
        
        a = n % 3
        lst.append(a)
        n = int(n / 3)
    
    if n > 0:
        lst.append(n)
    
    return list(reversed(lst))
    

def solution(n):
    answer = ''
    lst = deque(func(n))
    
    for i in range(1,len(lst)):
        if lst[i] == 0:
            if lst[i-1] == 1:
                lst[i-1] = 0

            elif lst[i-1] == 2:
                lst[i-1] = 1

            elif lst[i-1] == 4:
                lst[i-1] = 2
            lst[i] = 4

    for i in range(len(lst)-1, 0 ,-1):

        if lst[i] == 0:
            if lst[i-1] == 1:
                lst[i-1] = 0

            elif lst[i-1] == 2:
                lst[i-1] = 1

            elif lst[i-1] == 4:
                lst[i-1] = 2
            lst[i] = 4

    if lst[0] == 0:
        lst.popleft()
    
    for l in lst:
        answer += str(l)
    
    return answer