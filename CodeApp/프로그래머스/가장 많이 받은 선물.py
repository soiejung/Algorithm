# https://school.programmers.co.kr/learn/courses/30/lessons/258712
def solution(friends, gifts):
    answer = 0
    give = {}
    take = {}
    matrix = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
     
    point = []
    present = [0 for _ in range(len(friends))]
    for f in friends:
        give[f] = 0
        take[f] = 0
        
    for i in range(len(gifts)):
        who , to = gifts[i].split()
        give[who] += 1
        take[to] += 1
        
        for j in range(len(friends)):
            for p in range(len(friends)):
                if who == friends[j]:
                    if to == friends[p]:
                        matrix[j][p] += 1

    for key in give.keys():
        point.append(give[key] - take[key])
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if i != j:
                if matrix[i][j] > matrix[j][i]:
                    present[i] += 1
                
                elif matrix[i][j] < matrix[j][i]:
                    present[j] += 1
                    
                else:
                    if point[i] > point[j]:
                        present[i] += 1
                    elif point[i] < point[j] :
                        present[j] += 1
                    
    for i in range(len(present)):
        present[i] = int(present[i]/2)
    
    answer = max(present)

    return answer