# https://school.programmers.co.kr/learn/courses/30/lessons/138475
def solution(e, starts):
    answer = []
    # 약수의 갯수
    dp = [0] * (e+1)
    # 가장 많은 약수를 가진 index
    dp_idx = [0] * (e+1)
    
    # 약수의 갯수 빠르게 구하는 공식
    for i in range(2, e+1):
        for j in range(1, min(e//i+1, i)):
            dp[i*j] += 2
    for i in range(1, int(e**(1/2))+1):
        dp[i**2] +=1
    

    max_count = 0
    
    # 만약 약수의 갯수가 더 클 때 index값을 저장
    for i in range(e, 0, -1):
        if max_count <= dp[i]:
            max_count = dp[i]
            dp_idx[i] = i
        else:
            dp_idx[i] = dp_idx[i+1]
    
    for s in starts:
        answer.append(dp_idx[s])
    
    return answer