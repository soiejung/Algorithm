import re
def solution(files):
    answer = []
    FILE = []
    
    for f in files:
        
        head = re.split('[0-9]',f)[0]
        num = re.split('[^0-9]',f[len(head):])[0]
        
        if len(num) > 5:
            num = num[:5]
        
        
        if num.isdigit():
            FILE.append([head,num,f])

    FILE.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    for F in FILE:
        answer.append(F[2])
        
    return answer