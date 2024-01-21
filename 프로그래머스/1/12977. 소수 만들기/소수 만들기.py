import itertools
            
def solution(nums):
    answer = 0
    lst = []
    for a in itertools.combinations(nums, 3):
        num = 0
        for i in range(3):
            num += a[i] 
        lst.append(num)
    
    max_ = max(lst)
    matrix = [1 for _ in range(max_+1)]
    matrix[0], matrix[1] = 0, 0
    
    m = int(max_ ** 0.5)
    for i in range(2, m + 1):
        if matrix[i] == 1:           # i가 소수인 경우 
            for j in range(i+i, max_+1, i): # i이후 i의 배수들을 False 판정
                matrix[j] = 0
    
    
    for l in lst:
        if matrix[l] == 1:
            answer += 1
    return answer