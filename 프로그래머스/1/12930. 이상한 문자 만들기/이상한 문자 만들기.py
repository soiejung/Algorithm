import re
def solution(s):
    answer = ''
    up = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    low = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    for cur in re.split("[ ]",s):
        for i in range(len(cur)):
            if i%2 == 0:
                if cur[i] in low:
                    idx = low.index(cur[i])
                    answer += up[idx]
                else:
                    answer += cur[i]
            else:
                if cur[i] in up:
                    idx = up.index(cur[i])
                    answer += low[idx]
                else:
                    answer += cur[i]
        answer += ' '
    return answer[:-1]