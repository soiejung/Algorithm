def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}

    for i in range(len(genres)):
        dic1[genres[i]] = 0
        dic2[genres[i]] = []
    
    for i in range(len(genres)):
        dic1[genres[i]] += plays[i]
        dic2[genres[i]].append([plays[i],i])
    
    dic1 = sorted(dic1.items(),key = lambda x: x[1], reverse=True)

    for d1,d2 in dic1:
        for key, value in dic2.items():
            if key == d1:
                value.sort(key = lambda x: (x[0], -x[1]), reverse = True)

                if len(value) > 1:
                    for i in range(2):
                        answer.append(value[i][1])
                else:
                    answer.append(value[0][1])
                
    return answer