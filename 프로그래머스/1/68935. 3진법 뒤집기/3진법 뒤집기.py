def solution(n):
    answer = 0
    result = ''
    while n > 0:
        a = n%3
        result += str(a)
        n = n // 3
    
    answer = int(result,3)
    return answer