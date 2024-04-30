def solution(clothes):
    answer = 1
    dic = {}
    cnt = []
    for i in range(len(clothes)):
        dic[clothes[i][1]] = []
    
    for i in range(len(clothes)):
        dic[clothes[i][1]].append(clothes[i][0])
    
    for value in dic.values():
        cnt.append(len(value))
    
    for i in range(len(cnt)):
        answer *= (cnt[i] + 1)
    
    answer -= 1
    return answer