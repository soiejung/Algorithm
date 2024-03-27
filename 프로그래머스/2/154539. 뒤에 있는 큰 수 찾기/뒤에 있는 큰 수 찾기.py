from collections import deque
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)-1,-1,-1):
        
        # 만약 stack에 숫자가 존재하고, 존재한 숫자보다 내가 더 큰 숫자이면
        # 존재했던 숫자 제거
        while stack and numbers[i] >= stack[-1]:
            stack.pop()
        
        # stack의 제일 마지막 값이 가장 가까우면서 자신보다 큰 수
        if stack:
            answer[i] = stack[-1]
        
        # 나 자신 추가해주기
        stack.append(numbers[i])
  
    return answer