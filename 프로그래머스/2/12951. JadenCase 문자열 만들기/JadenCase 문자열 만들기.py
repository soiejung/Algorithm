
def solution(s):
    answer = ''
    words = s.split(" ")
    
    for i in range(len(words)):
        answer += words[i].capitalize()
        answer += ' '
        
        
    return answer[:-1]