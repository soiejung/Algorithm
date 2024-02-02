from collections import deque
def solution(n, words):
    answer = []
    s = deque()
    w = []
    

    for i in range(len(words)):
        if not s:
            s.append(words[i])
            w.append(words[i])
            
        else:
            
            if s[-1][-1] == words[i][0] and words[i] not in w:
                s.pop()
                s.append(words[i])
                
                
            else:
                answer.append(i%n+1)
                answer.append(i//n+1)
                break
                
            w.append(words[i])
    
    if not answer:
        return [0,0]
    else:
        return answer