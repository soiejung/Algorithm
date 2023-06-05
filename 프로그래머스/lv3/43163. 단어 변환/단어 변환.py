from collections import deque
def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin,0))
    visited = [0] * len(words)
    lst = deque()
    
    while queue:
        
        if queue:
            b, depth = queue.popleft()
            if b == target:
                return depth
        for i in range(len(words)):
            count = 0
            for j in range(len(words[i])):
                if not visited[i]:
                    if words[i][j] != b[j]:
                        count += 1
            if count == 1:
                queue.append((words[i], depth+1))
                visited[i] = 1
                                
    return answer