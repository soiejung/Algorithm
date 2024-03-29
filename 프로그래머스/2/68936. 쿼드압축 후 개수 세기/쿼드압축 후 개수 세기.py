def recur(arr, result):
    
    if not arr:
        return -1
    
    n = int(len(arr)/2)
    c1, c2 = 0, 0
    
    if len(arr) > 1:
        
        check = 1
        c = arr[0][0]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if c != arr[i][j]:
                    check = 0
                    break
        
        if check:
            if c == 0:
                result.append([1,0])
            else:
                result.append([0,1])
            
            return
    
        else:
                
            for i in range(0,len(arr),n):
                for j in range(0,len(arr),n):
                    check = arr[i][j]
                    a = []
                    flag = 1
                    for k in range(i,i+n):
                        for p in range(j,j+n):
                            if arr[k][p] != check:
                                flag = 0
                                break
                    if flag:
                        if check == 0:
                            c1 += 1
                        else:
                            c2 += 1


                    else:

                        for k in range(i,i+n):
                            lst = []
                            for p in range(j,j+n):
                                lst.append(arr[k][p])
                            a.append(lst)
                        recur(a,result)

            result.append([c1,c2])
    else:
        if arr[0] == 0:
            c1 += 1
        else:
            c2 += 1
        
        result.append([c1,c2])
    
    
    
def solution(arr):
    answer = []
    result = []
    recur(arr,result)
    c1, c2 = 0, 0
    for r in result:
        c1 += r[0]
        c2 += r[1]
    
    answer.append(c1)
    answer.append(c2)
    return answer
