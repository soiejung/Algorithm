def solution(arr):
    answer = 0
    
    for a in arr:
        answer += a
    return answer/len(arr)