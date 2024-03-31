from itertools import combinations
def solution(orders, course):
    answer = []
    alpha = []
    result = []

    for c in course:
        lst = []
        for order in orders:
            for com in combinations(order,c):
                s = ''
                com = sorted(com)
                for i in range(len(com)):
                    s += str(com[i])
                if s not in lst:
                    lst.append(s)
        alpha.append(lst)
    
    for i in range(len(alpha)):
        r = []
        for j in range(len(alpha[i])):
            count = 0
            for o in orders:
                flag = 1
                for k in range(len(alpha[i][j])):
                    if alpha[i][j][k] not in o:
                        flag = 0
                        break
                if flag:
                    count += 1
                
            if count >= 2:
                r.append([alpha[i][j],count])
        
        if r:
            r.sort(key = lambda x: x[1], reverse = True)
            max_ = r[0][1]
            for a in range(len(r)):
                if r[a][1] < max_:
                    break
                else:
                    result.append(r[a][0])
    
    result.sort()
    return result