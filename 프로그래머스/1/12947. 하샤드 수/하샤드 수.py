def solution(x):
    answer = True
    
    str_x = str(x)
    total = 0
    for i in range(len(str_x)):
        total += int(str_x[i])
    
    if x % total == 0:
        return True
    else:
        return False
