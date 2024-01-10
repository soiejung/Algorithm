#https://www.acmicpc.net/problem/2503

import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999999)
def recur(hint_idx, number, answer):

    # 만약에 힌트에 통과했다면
    if hint_idx == N:
        answer += 1
        recur(0, number+1, answer)
        return

    if number == 1000:
        return
    
    check = list(hint[hint_idx][0])
    strike = int(hint[hint_idx][1])
    ball = int(hint[hint_idx][2])

    print(check, strike, ball)
    strike_count = 0
    ball_count = 0
    if str(number)[0] == check[0]:
        strike_count += 1
    
    if str(number)[1] == check[1]:
        strike_count += 1
    
    if str(number)[2] == check[2]:
        strike_count += 1

    if str(number)[0] == check[1] or str(number)[0] == check[2]:
        ball_count += 1
    
    if str(number)[1] == check[0] or str(number) == check[2]:
        ball_count += 1
    
    if str(number)[2] == check[0] or str(number)[2] == check[1]:
        ball_count += 1

    # 만약 힌트에 통과하지 못했다면 다음 숫자 진행
    if strike != strike_count:
        recur(0, number+1, answer)
    
    if ball != ball_count:
        recur(0, number+1, answer)    
    
    recur(hint_idx+1, number, answer)


N = int(input())
hint = [list(map(str,input().split())) for _ in range(N)]
answer = 0
recur(0, 100, answer) # 0은 hint의 숫자, 100은 시작 숫자
print(answer)

"""
# 세자리 수 만들기
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):

            count = 0

            # 서로 다른 숫자 세 대로 구성됨
            if i == j or j == k or k == i:
                continue

            for h in hint:

                check = list(h[0]) # ['1', '2', '3']
                strike = int(h[1])
                ball = int(h[2])

                strike_count = 0
                ball_count = 0

                # 각 자리에서 똑같은 수가 있다면 strike 수를 세준다
                if i == int(check[0]):
                    strike_count += 1
            
                if j == int(check[1]):
                    strike_count += 1

                if k == int(check[2]):
                    strike_count += 1

                # 각 자리 이외에 똑같은 수가 있다면 ball 수를 세준다
                if i == int(check[1]) or i == int(check[2]):
                    ball_count += 1
                
                if j == int(check[0]) or j == int(check[2]):
                    ball_count += 1
                
                if k == int(check[0]) or k == int(check[1]):
                    ball_count += 1
                

                # strike 숫자와 센 strike 숫자가 같지 않으면 종료
                if strike != strike_count:
                    break
                
                # ball 숫자와 센 ball 숫자가 같지 않으면 종료
                if ball != ball_count:
                    break
                
                # hint의 한 경우에서 strike와 ball 숫자가 센 숫자들과 같으면 +1
                count += 1

            # 주어진 모든 힌트에서 조건을 만족하면 가능성이 있는 수
            if count == N:
                answer += 1
                
print(answer)
"""
