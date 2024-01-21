def solution(n, m, section):
    answer = 1
    
    first = min(section)
    
    for s in section:
        if s > first + m - 1:
            answer += 1
            first = s
    return answer