import re
def solution(record):
    answer = []
    user = {}
    chat = []

    for r in record:
        
        behavior = r.split(' ')[0]
        u_id = r.split(' ')[1]
        
        
        if behavior == "Leave":
            chat.append([u_id,1])
        
        else:
            name = r.split(' ')[2]
            user[u_id] = name
            if behavior == "Enter":
                chat.append([u_id,0])
    
    for c in chat:
        if c[1] == 0:
            s = user[c[0]]+"님이 들어왔습니다."
            answer.append(s)
            
        elif c[1] == 1:
            s = user[c[0]]+"님이 나갔습니다."
            answer.append(s)
            
    return answer