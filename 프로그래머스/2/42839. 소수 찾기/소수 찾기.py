import itertools
def solution(numbers):
    answer = 0
    num = []
    lst = []
    for n in numbers:
        num.append(n)
    
    for n in numbers:
        if int(n) not in lst:
            lst.append(int(n))
            
    for i in range(2,len(num)+1):

        for nn in itertools.permutations(num,i):
            n = ''
            for j in range(len(nn)):
                n += str(nn[j])
            
            if int(n) not in lst:
                lst.append(int(n))
    
    
    max_ = max(lst)
    
    for l in lst:
        flag = 1
        if l == 0 or l == 1:
            continue
            
        for i in range(2,int(l**(1/2))+1):
            if l % i == 0:
                flag = 0
                break
        if flag:
            answer += 1

    return answer