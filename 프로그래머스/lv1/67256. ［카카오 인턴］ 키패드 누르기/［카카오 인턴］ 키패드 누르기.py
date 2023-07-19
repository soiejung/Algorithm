def solution(numbers, hand):
    answer = ''
    
    dic = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
    
    last_l = dic['*']
    last_r = dic['#']
    
    for n in numbers:
        if n==1 or n==4 or n==7:
            answer += 'L'
            last_l = dic[n]
        elif n==3 or n==6 or n==9:
            answer += 'R'
            last_r = dic[n]
        else:
            xl, yl = last_l[0], last_l[1]
            xr, yr = last_r[0], last_r[1]
            x, y = dic[n][0], dic[n][1]
            
            # 유클리드하면 거리 다른 경우 생김. 맨하탄 거리로 해야함
            if abs(x-xl) + abs(y-yl) > abs(x-xr) + abs(y-yr):
                answer += 'R'
                last_r = dic[n]
            elif abs(x-xl) + abs(y-yl) < abs(x-xr) + abs(y-yr):
                answer += 'L'
                last_l = dic[n]
            else:
                if hand == 'right':
                    answer += 'R'
                    last_r = dic[n]
                else:
                    answer += 'L'
                    last_l = dic[n]
    return answer