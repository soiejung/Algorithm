def solution(n):
    answer = 0
    
    if n < 2:
        return n
    
    else:
        for i in range(1, int(n**(1/2))+1):
            if n%i == 0:
                if n//i != i:
                    answer += i
                    answer += n//i
                else:
                    answer += i

        return answer