
def solution(word):
    answer = 0
    lst = []
    words = 'AEIOU'
    
    def dfs(cnt, w):
        if cnt == 5:
            return
        for i in range(len(words)):
            lst.append(w+words[i])
            dfs(cnt+1,w+words[i])
    
    dfs(0,'')
    answer = lst.index(word)+1
    return answer