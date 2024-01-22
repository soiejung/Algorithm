# https://school.programmers.co.kr/learn/courses/30/lessons/132267#
def solution(a, b, n):
    answer = 0
    now = n
    while True:
        
        if now < 2:
            break
            
        if now >= a:
            coke = (now//a)*b
            answer += coke
            now = coke + now%a
        else:
            break

    return answer