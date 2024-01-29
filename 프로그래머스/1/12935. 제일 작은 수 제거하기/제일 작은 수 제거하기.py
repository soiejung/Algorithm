def solution(arr):
    answer = []
    
    if len(arr) < 2:
        answer.append(-1)
    else:
        min_ = min(arr)
        idx = arr.index(min_)
        arr.pop(idx)
        answer = arr
    return answer