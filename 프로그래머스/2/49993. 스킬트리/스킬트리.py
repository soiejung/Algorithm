def solution(skill, skill_trees):
    answer = 0
    
    skill = list(skill)
    
    
    for skills in skill_trees:
        stack = []
        
        for s in skills:
            if s in skill:
                stack.append(s)
        
        flag = 1
        
        for i in range(len(stack)):
            if stack[i] != skill[i]:
                flag = 0
        
        if flag:
            answer += 1
                
            
    return answer