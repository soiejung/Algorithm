from collections import deque
def solution(numbers, target):
    answer = 0
    lst = deque()
    numbers = deque(numbers)
    temp = numbers.popleft()
    size = len(numbers)
    lst.append(temp)
    lst.append(-1*temp)

    while True:
        
        if numbers:
            length = len(lst)

            tmp = numbers.popleft()
            for i in range(length):
                l = lst.popleft()
                lst.append(l+tmp)
                lst.append(l-tmp)

        else:
            break

        
    for l in lst:
        if l == target:
            answer += 1
    return answer