def solution(numbers):
    from itertools import permutations
    import math
    
    answer = []
    l = []
    num = []
    l.extend(numbers)
    
    for i in range(1,len(numbers)+1):
        num += list(permutations(l,i))
        
    a = [int(''.join(n)) for n in num]
    
    for b in a:
        
        if b < 2:
            continue
        check = True
        for k in range(2, int(math.sqrt(b))+1):
            if b % k == 0:
                check = False
                break
            else:
                check = True
            
        if check:
            answer.append(b)

    return len(set(answer))