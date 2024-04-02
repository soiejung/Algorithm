def solution(numbers, target):
    answer = 0
    
    def cal(idx,total):
        nonlocal answer
        
        if idx == len(numbers)-1:
            if target == total:
                answer += 1
            return
    
        cal(idx+1,total + numbers[idx])
        cal(idx+1, total - numbers[idx])
    
    cal(-1,0)
    return answer