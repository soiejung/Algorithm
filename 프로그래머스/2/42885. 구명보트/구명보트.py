from collections import deque
def solution(people, limit):
    answer = 0
    
    people.sort(reverse = True)
    people = deque(people)
    
    while people:
        
        if people:
            p = people.popleft()
            if people:
                m = people.pop()
                if p + m > limit:
                    answer += 1
                    people.append(m)
                else:
                    answer += 1
            else:
                answer += 1
                

            
    return answer