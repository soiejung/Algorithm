def solution(genres, plays):
    answer = []
    sum_dict = {}
    
    for i in range(len(genres)):
        if genres[i] in sum_dict.keys():
            s = sum_dict[genres[i]]
            sum_dict[genres[i]] += plays[i]
        else:
            sum_dict[genres[i]] = plays[i]
      
    sum_dict = sorted(sum_dict.items(), key = lambda x : x[1], reverse = True)
    print(sum_dict)
    dict = {}
    lst = []
    for genre, play in sum_dict:
        temp = []
        for i in range(len(genres)):
            if genre == genres[i]:
                temp.append((plays[i], i))
        temp.sort(key = lambda x : (x[0],-x[1]), reverse = True)
        count=0
        for t in temp:
            if count ==2:
                break
            else:
                lst.append(t)
                count += 1
    
    for l in lst:
        answer.append(l[1])
        
    return answer