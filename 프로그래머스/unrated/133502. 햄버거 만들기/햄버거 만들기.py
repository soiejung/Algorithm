from collections import deque
def solution(ingredient):
    answer = 0
    stack = deque()
    ## 1: 빵, 2: 야채, 3: 고기
    
    lst = [1,2,3,1]
    
    for i in ingredient:
        if not stack:
            stack.append(i)
        else:
            if i==1:
                if 1 in stack:
                    if len(stack)>=3 and stack[-1] == 3 and stack[-2] == 2 and stack[-3] == 1:
                        answer += 1
                        stack.pop()
                        stack.pop()
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            else:
                stack.append(i)
                    
    return answer