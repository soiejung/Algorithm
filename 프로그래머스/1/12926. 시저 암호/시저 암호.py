def solution(s, n):
    answer = ''
    up = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    low = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    for i in range(len(s)):
        
        if s[i] in up:
            idx = up.index(s[i])
            answer += up[(idx+n)%26]
        elif s[i] in low:
            idx = low.index(s[i])
            answer += low[(idx+n)%26]
        else:
            answer += s[i]
    
    return answer