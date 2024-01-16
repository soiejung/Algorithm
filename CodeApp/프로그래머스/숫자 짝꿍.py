# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    answer = ''
    lst = []
    
    # 1~9에 해당하는 숫자 있으면 세기
    x = [0 for _ in range(10)]
    y = [0 for _ in range(10)]
    
    for i in range(len(X)):
        if X[i] == '0':
            x[0] += 1
        elif X[i] == '1':
            x[1] += 1
        elif X[i] == '2':
            x[2] += 1
        elif X[i] == '3':
            x[3] += 1
        elif X[i] == '4':
            x[4] += 1
        elif X[i] == '5':
            x[5] += 1
        elif X[i] == '6':
            x[6] += 1
        elif X[i] == '7':
            x[7] += 1
        elif X[i] == '8':
            x[8] += 1
        elif X[i] == '9':
            x[9] += 1
        
    for i in range(len(Y)):
        if Y[i] == '0':
            y[0] += 1
        elif Y[i] == '1':
            y[1] += 1
        elif Y[i] == '2':
            y[2] += 1
        elif Y[i] == '3':
            y[3] += 1
        elif Y[i] == '4':
            y[4] += 1
        elif Y[i] == '5':
            y[5] += 1
        elif Y[i] == '6':
            y[6] += 1
        elif Y[i] == '7':
            y[7] += 1
        elif Y[i] == '8':
            y[8] += 1
        elif Y[i] == '9':
            y[9] += 1

# 1~9 숫자 중 공통으로 들어있는 숫자 구하기
    for i in range(10):
        if x[i] != 0 and y[i] != 0:
            for j in range(min(x[i],y[i])):
                str_i = str(i)
                lst.append(str_i)

    lst.sort(reverse=True)
    
    # 공통으로 들어있는 숫자가 없을 때 '-1' 리턴
    if len(lst) == 0:
        return '-1'
    else:
        # 공통인 숫자가 0밖에 없을 때 '0' 리턴
        if lst[0] == '0':
            return '0'
        else:
            for l in lst:
                answer += l
    
    return answer