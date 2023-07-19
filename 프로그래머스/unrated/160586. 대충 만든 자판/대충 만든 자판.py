def solution(keymap, targets):
    answer = []
    
    dic = {}
    for k in keymap:
        for i in range(len(k)):
            dic[k[i]] = len(k)
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if j+1 < dic[keymap[i][j]]: 
                dic[keymap[i][j]] = j+1

    
    for t in targets:
        count = 0
        for i in range(len(t)):
            if t[i] in dic.keys():
                count += dic[t[i]]
            else:
                count = -1
                break
        answer.append(count)

    return answer