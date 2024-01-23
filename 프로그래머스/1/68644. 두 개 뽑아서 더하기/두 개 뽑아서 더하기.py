import itertools
def solution(numbers):
    answer = []
    
    for n in itertools.combinations(numbers,2):
        sum_ = 0
        for i in range(len(n)):
            sum_ += n[i]
        if sum_ not in answer:
            answer.append(sum_)
        
    answer.sort()
    return answer