def solution(answers):
    result = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for idx, answer in enumerate(answers):
        if answer == a1[idx%len(a1)]:
            score[0] +=1
        if answer == a2[idx%len(a2)]:
            score[1] += 1
        if answer == a3[idx%len(a3)]:
            score[2] += 1
        
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
            
    return result