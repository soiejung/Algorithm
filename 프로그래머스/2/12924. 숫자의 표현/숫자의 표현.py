def solution(n):
    answer = 1
    # 자기자신
    for i in range(1, int(n/2)+1):
        
        total = 0
        
        # i = 1 -> 1 + 2 + 3 + 4 + 5 = 15
        # i = 2 -> 2 + 3 + .... 
        # i = 3 -> 3 + 4 + ....
        # i = 4 -> 4 + 5 + 6 = 15
        # i = 5 -> 5 + 6 + ...
        # i = 6 -> 6 + 7 + ...
        # i = 7 -> 7 + 8 = 15
        
        while total < n:
            
            total += i
            
		    # 만약 합이 n과 같은 경우가 있다면 + 1
            if total == n:
                answer += 1
                break

            # 다음 숫자로 넘어가기
            i+=1
        
    return answer