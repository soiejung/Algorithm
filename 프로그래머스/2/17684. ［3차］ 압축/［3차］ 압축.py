from collections import deque
def solution(msg):
    answer = []
    num_dic = {}
    alpha_dic = {}
    alpha = ord('A')
    last_idx = 27
    for i in range(1, 27):
        num_dic[i] = chr(alpha)
        alpha_dic[chr(alpha)] = i
        alpha += 1

    msg = deque(msg)
    w = ''
    while msg:
        
        if msg:
            
            w = w + msg.popleft()
            if msg:
                c = msg[0]
                if w + c not in alpha_dic.keys():
                    alpha_dic[w+c] = last_idx
                    num_dic[last_idx] = w+c
                    answer.append(alpha_dic[w])
                    last_idx += 1
                    w = ''
                    
                else:
                    w = w
            else:
                answer.append(alpha_dic[w])
        else:
            break
                    
            
    return answer