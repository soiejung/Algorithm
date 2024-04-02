def solution(numbers, target):

    def cal(idx,total):
        nonlocal answer
        if idx == len(numbers)-1:
            if total == target:
                answer += 1
            return
        
        cal(idx+1, total + numbers[idx])
        cal(idx+1, total - numbers[idx])
        
    answer = 0
    cal(-1,0)
        
    return answer