def solution(n, left, right):
    answer = []
            
    idx1 = int(left / n)
    idx2 = left % n
    
    idx3 = int(right / n)
    idx4 = right % n
    
    if idx1 == idx3:
        for j in range(idx2, idx4+1):
            answer.append(max(idx1,j)+1)
    else:
        for i in range(idx1, idx3+1):
            if i == idx1:
                for j in range(idx2,n):
                    answer.append(max(i,j)+1)
            elif i == idx3:
                for j in range(idx4+1):
                    answer.append(max(i,j)+1)
            else:
                for j in range(n):
                    answer.append(max(i,j)+1)
                
    
    return answer