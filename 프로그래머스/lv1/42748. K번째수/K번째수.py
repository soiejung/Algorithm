def solution(array, commands):
    answer = []
    n = len(commands)
    list = []
    for l in range(n):
        i, j, k = commands[l]
        list = array[i-1: j]
        list.sort()
        answer.append(list[k-1])
        
    return answer