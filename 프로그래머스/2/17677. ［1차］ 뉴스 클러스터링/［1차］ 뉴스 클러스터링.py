from collections import deque
def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    set1 = []
    set2 = []
    
    for i in range(len(str1)-1):
        set1.append(str1[i]+str1[i+1])
    
    for i in range(len(str2)-1):
        set2.append(str2[i]+str2[i+1])

    ss1 = []
    ss2 = []
    for s in set1:
        if s.isalpha():
            ss1.append(s)
    
    for s in set2:
        if s.isalpha():
            ss2.append(s)

    
    intersec = []
    union = []
    tmp = []
    
    for s in ss1:
        if s not in ss2:
            union.append(s)
        else:
            tmp.append(s)
    
    for s in ss2:
        if s not in ss1:
            union.append(s)
    
    tmp = set(tmp)
    for t in tmp:
        c1 = ss1.count(t)
        c2 = ss2.count(t)
        max_ = max(c1,c2)
        min_ = min(c1,c2)

        for _ in range(max_):
            union.append(t)
        for _ in range(min_):
            intersec.append(t)
    
    
    if len(union) == 0 and len(intersec) == 0:
        return 65536
    
    answer = int(len(intersec) / len(union) * 65536)
    return answer