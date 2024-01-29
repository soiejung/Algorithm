def solution(arr):
    answer = []
    size = len(arr)
    answer.append(arr[0])
    for i in range(1,size):
        
        if answer[-1] != arr[i]:
            answer.append(arr[i])
            
    return answer