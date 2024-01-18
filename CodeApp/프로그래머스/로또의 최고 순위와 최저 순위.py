# https://school.programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    answer = []
    count = 0
    high , low = 0, 0
    lottos.sort()
    win_nums.sort()
    
    for l in lottos:
        for w in win_nums:
            if l == w:
                count += 1

    x = 0
    for l in lottos:
        if l == 0:
            x += 1
            
    if count < 2:
        low = 6
    else:
        low = 7 - count
    
    y = count + x
    
    if y < 2:
        best = 6
    else:
        best = 7 - y
    
    answer = [best, low]
    return answer