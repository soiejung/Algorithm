def solution(s):
    answer = []
    dic = {}
    
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
            dic[s[i]] = i
        else:
            idx = dic[s[i]]
            answer.append(i-idx)
            dic[s[i]] = i

    return answer