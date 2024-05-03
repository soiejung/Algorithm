def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3= [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1, s2, s3 = 0, 0, 0
    s = []
    for i in range(len(answers)):
        if answers[i] == a1[i%len(a1)]:
            s1 += 1
        if answers[i] == a2[i%len(a2)]:
            s2 += 1
        if answers[i] == a3[i%len(a3)]:
            s3 += 1
    
    s.append(s1)
    s.append(s2)
    s.append(s3)
    
    for i in range(3):
        if s[i] == max(s):
            answer.append(i+1)
    
            
    return answer