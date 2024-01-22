# https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for i in range(len(name)):
        dic[name[i]] = yearning[i]

    
    for p in photo:
        sum_ = 0
        for pp in p:
            if pp in dic.keys():
                sum_ += dic[pp]
        answer.append(sum_)
    return answer