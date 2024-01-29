import itertools
def solution(number):
    answer = 0
    
    for n in itertools.combinations(number,3):
        sum = 0
        for i in range(3):
            sum += n[i]
        if sum == 0:
            answer += 1
            
    return answer