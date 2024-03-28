def solution(land):
    answer = 0
    
    
    for i in range(1,len(land)):
        for j in range(4):
            tmp = land[i-1][j]
                            
            # 이전에 선택한 열을 연속해서 밟지 않도록
            land[i-1][j] = -1
            
            # 이전에 선택한 열을 제외한 값들 중 최대 값
            land[i][j] += max(land[i-1][0], land[i-1][1], land[i-1][2], land[i-1][3])
            
            # 값 원래대로 돌려주기
            land[i-1][j] = tmp
    
    answer = max(land[-1])
            
    
    return answer