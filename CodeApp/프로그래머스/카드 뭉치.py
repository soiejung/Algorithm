# https://school.programmers.co.kr/learn/courses/30/lessons/159994#
from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    
    g = deque(goal)
    c1 = deque(cards1)
    c2 = deque(cards2)
    cnt = 0
    while g:
        if g:
            first = g[0]
            if c1:
                if first == c1[0]:
                    c1.popleft()
                    g.popleft()
            if c2:
                if first == c2[0]:
                    c2.popleft()
                    g.popleft()
            cnt += 1
        if cnt == len(goal):
            break
            
    if g:
        return "No"
    else:
        return "Yes"
