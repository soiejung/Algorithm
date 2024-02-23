import re
def solution(s):
    answer = []
    lst = []
    num = []
    for cur in re.split('[}]',s):
        if not cur:
            continue
        else:
            if cur not in lst:
                lst.append(cur)
                
    for l in lst:
        lst1 = []
        for cur in re.split('[{,]',l):
            if not cur:
                continue
            else:
                lst1.append(int(cur))
        num.append(lst1)

    num.sort(key=len)
    
    # answer에 같은 문자가 있으면 n에서 지워준다.
    # 지워준 후 남은 하나의 숫자를 answer에 저장
    for n in num:
        for i in answer:
            n.remove(i)
        answer.append(n[0])
        
    return answer