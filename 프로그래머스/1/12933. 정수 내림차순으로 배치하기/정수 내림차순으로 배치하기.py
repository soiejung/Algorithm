def solution(n):
    answer = 0
    
    str_n = str(n)
    return int(''.join(sorted(str_n, reverse=True)))