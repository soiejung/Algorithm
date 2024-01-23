def binary(n,number):
    
    a = 0
    result = []
    if number < 2:
        result.append(number)
    
    else:
        while number>1:
            a = number % 2
            result.append(a)
            number = number//2
            if number == 1:
                result.append(1)
                break
    cnt = len(result)
    while cnt<n:
        result.append(0)
        cnt+=1
    return result

    

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        result1 = binary(n,arr1[i])
        result2 = binary(n,arr2[i])
        result = []
        for r in range(n):
            result.append(result1[r]+result2[r])

        
        str_result = ""
        for j in range(len(result)-1,-1,-1):
            if result[j] == 0:
                str_result += ' '
            else:
                str_result += '#'
        answer.append(str_result)
    
    return answer