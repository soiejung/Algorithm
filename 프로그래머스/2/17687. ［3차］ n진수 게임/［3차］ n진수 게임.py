def func(num, n):
    
    lst = []
    
    if num == 0:
        return [0]
    
    if num == 1:
        return [1]
    
    while num > 1:
        a = num % n
        if a >= 10 and a <= 15:
            for i in range(10, 16):
                if a == i:
                    lst.append(chr(a+55))
                    break
        else:
            lst.append(a)
        num = int(num/n)

    if num > 0:
        lst.append(num)

    return list(reversed(lst))
        
        

def solution(n, t, m, p):
    answer = ''
    lst = []
    for i in range(t*m):
        lst += func(i,n)
    
    pp = p-1
    
    while len(answer) < t:
        answer += str(lst[pp])
        pp += m
            
    return answer