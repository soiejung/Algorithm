def solution(weights):

    answer = 0
    visited = [-1 for _ in range(40001)]
    same = [-1 for _ in range(1001)]
    cnt = 0
    
    for i in range(len(weights)):
        same[weights[i]] += 1
        cnt += same[weights[i]]
        same_cnt = same[weights[i]]
        
        for j in range(2,5):
            visited[weights[i]*j] += 1
            cnt += (visited[weights[i]*j] - same_cnt)

        
        
    
    return cnt