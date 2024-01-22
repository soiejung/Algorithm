# https://school.programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    answer = ''
    
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    d = 0
    for i in range(a-1):
        d += days[i]
    
    d += b
    answer = day[d%7]
    return answer