def solution(brown, yellow):
    answer = []
    num = brown - 4 # 가장자리 4개 제외
    
    # a 가 세로, b가 가로
    for a in range(1, yellow+1):
        
        if yellow%a != 0:
            continue
        else:
            b = yellow/a
            if 2*a + 2*b == num:
                
                answer = [int(b)+2,int(a)+2]
                break
    return answer