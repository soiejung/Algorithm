def solution(numbers):
    answer = ''
    
    str_numbers = []
    
    flag = 0
    for n in numbers:
        if n != 0:
            flag = 1
            break
    
    if flag:
        for n in numbers:
            str_numbers.append(str(n))

        str_numbers.sort(key = lambda x: x*3, reverse = True)

        for s in str_numbers:
            answer += s
    else:
        answer = "0"
    return answer