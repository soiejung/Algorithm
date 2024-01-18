# https://school.programmers.co.kr/learn/courses/30/lessons/17682
import re
def solution(dartResult):
    answer = 0
    number = []
    area = []
    # S, D, T, *, # 를 기준으로 문자열 쪼개기 -> 숫자만 담기게
    for cur in re.split('[S,D,T,*, #]', dartResult):
        if not cur:
            continue
        number.append(int(cur))
    
    # 숫자를 기준으로 문자열 쪼개기 -> S, D, T, *, # 만 담기게
    for cur in re.split('[1,2,3,4,5,6,7,8,9,0]', dartResult):
        if not cur:
            continue
        area.append(cur)
    
    # 각 단위별로 계산한 결과 저장할 문자열
    result = [0 for _ in range(len(number))]
    
    for i in range(len(number)):
        if 'S' in area[i]:
            result[i] = number[i] ** 1
        if 'D' in area[i]:
            result[i] = number[i] ** 2
        if 'T' in area[i]:
            result[i] = number[i] ** 3
        if '*' in area[i]:
            result[i] = result[i] * 2
            if i>0:
                result[i-1] = result[i-1] * 2
        if '#' in area[i]:
            result[i] *= -1
        
    for r in result:
        answer += r
    return answer