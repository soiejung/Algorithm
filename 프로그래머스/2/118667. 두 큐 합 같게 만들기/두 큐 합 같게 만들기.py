from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    size1 = len(queue1)
    total1, total2 = 0, 0
    
    for q in queue1:
        total1 += q
    
    for q in queue2:
        total2 += q
        
    mid = int((total1 + total2) / 2)
    
    while True:
        
        if len(queue1) == 0 or len(queue2) == 0:
            return -1
        
        # 무한 swap 방지
        if answer > size1 * 4:
            return -1
        
        if total1 == total2:
            break
        
        if total1 > total2:
            if queue1:
                q = queue1.popleft()
                queue2.append(q)
                total1 -= q
                total2 += q
                answer += 1

        elif total1 < total2:
            if queue2:
                q = queue2.popleft()
                queue1.append(q)
                total1 += q
                total2 -= q
                answer += 1
    

    return answer