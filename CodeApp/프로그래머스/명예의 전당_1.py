# https://school.programmers.co.kr/learn/courses/30/lessons/138477#
import heapq
def solution(k, score):
    answer = []
    
    lst = []
    lst.append(score[0])
    answer.append(score[0])
    for i in range(1,len(score)):
        heapq.heapify(lst)
        min_ = lst[0]
        if len(lst) == k:
            if score[i] > min_:
                heapq.heappop(lst)
                heapq.heappush(lst,score[i])
                min_ = lst[0]
        elif len(lst) < k:
            heapq.heappush(lst,score[i])
            min_ = lst[0]
        answer.append(min_)
            
        
    return answer