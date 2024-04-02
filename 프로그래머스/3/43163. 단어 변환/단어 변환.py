from collections import deque
def same_count(word1,word2):
    
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    
    return cnt

def solution(begin, target, words):
    answer = len(words)
    
    if target not in words:
        return 0
    
    queue = deque()
    visited = [0 for _ in range(len(words))]
    
    queue.append([begin,0])
    
    while queue:
        if queue:
            word, depth = queue.popleft()

            if word == target:
                return depth
            
            for i in range(len(words)):
                if not visited[i] and same_count(word,words[i]) == 1:
                    queue.append([words[i],depth+1])
                    visited[i] = 1
    
    return answer