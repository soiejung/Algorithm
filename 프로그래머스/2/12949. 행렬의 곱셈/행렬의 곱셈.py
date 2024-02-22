def solution(arr1, arr2):
    answer = [[]]
    m, n, k = 0, 0, 0
    
    for i in range(len(arr1)):
        lst = []
        for k in range(len(arr2[0])):
            total = 0
            for j in range(len(arr1[0])):
                total += arr1[i][j] * arr2[j][k]
            lst.append(total)
        answer.append(lst)
        
    
    return answer[1:]