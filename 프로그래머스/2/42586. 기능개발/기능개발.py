from collections import deque
def solution(progresses, speeds):
    answer = []
    days = deque()
    
    for i in range(len(progresses)):
        d = 100 - progresses[i]
        if d%speeds[i] == 0:
            days.append(int(d/speeds[i]))
        else:
            days.append(int(d/speeds[i])+1)
        
    start = days.popleft()
    cnt = 1
    while days:
        if days:
            if start >= days[0]:
                cnt += 1
                days.popleft()
            else:
                answer.append(cnt)
                cnt = 1
                if days:
                    start = days.popleft()

    
    answer.append(cnt)
            
    
    return answer