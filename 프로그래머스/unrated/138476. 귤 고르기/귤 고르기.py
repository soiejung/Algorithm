from itertools import combinations
def solution(k, tangerine):
    answer = 0
    dic = {}
    lst = []
    
    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
    
    sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    total = 0
    for s in sorted_dic:

        total += s[1]
        answer += 1
        if total >= k:
            return answer
            
