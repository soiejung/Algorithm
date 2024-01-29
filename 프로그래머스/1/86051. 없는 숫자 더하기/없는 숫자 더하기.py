def solution(numbers):
    answer = -1
    
    total = 0
    for n in numbers:
        total += n
    
    answer = 45 - total
    return answer