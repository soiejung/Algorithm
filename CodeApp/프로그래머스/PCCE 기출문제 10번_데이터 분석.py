# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = []
    idx = 0
    if ext == "code":
        idx = 0
    elif ext == "date":
        idx = 1
    elif ext == "maximum":
        idx = 2
    else:
        idx = 3
        
    for d in data:
        if d[idx] < val_ext:
            answer.append(d)
    
    if sort_by == "code":
        answer.sort(key=lambda x:(x[0],x[1],x[2],x[3]))
    elif sort_by == "date":
        answer.sort(key=lambda x:(x[1],x[0],x[2],x[3]))
    elif sort_by == "maximum":
        answer.sort(key=lambda x:(x[2],x[0],x[1],x[3]))
    else:
        answer.sort(key=lambda x:(x[3],x[0],x[1],x[2]))
        
    return answer