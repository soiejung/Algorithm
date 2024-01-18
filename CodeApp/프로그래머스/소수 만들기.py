# https://school.programmers.co.kr/learn/courses/30/lessons/12977
import itertools
            
def solution(nums):
    answer = 0
    lst = []
    # 3개를 골라 더했을 때 나오는 수 모두 구하기
    for a in itertools.combinations(nums, 3):
        num = 0
        for i in range(3):
            num += a[i] 
        lst.append(num)
    
    # 그 중 가장 큰 수 고르기
    max_ = max(lst)
    # 소수 판별을 위해 필요한 배열
    matrix = [1 for _ in range(max_+1)]
    # 0과 1은 소수가 아님
    matrix[0], matrix[1] = 0, 0
    

    m = int(max_ ** 0.5)
    for i in range(2, m + 1):
        if matrix[i] == 1:           # i가 소수인 경우 
            for j in range(i+i, max_+1, i): # i이후 i의 배수들을 False 판정
                matrix[j] = 0
    
    
    # l이 소수인경우 1, 아닌 경우 0 카운트 해주기
    for l in lst:
        if matrix[l] == 1:
            answer += 1
    return answer