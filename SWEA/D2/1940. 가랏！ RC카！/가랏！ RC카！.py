T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N = int(input())
    now = 0
    distance = 0
    for i in range(N):
        lst = list(map(int,input().split()))

        plus_minus = lst[0]
        if len(lst)==2:
        	speed = lst[1]
        else:
            speed = now

        if plus_minus == 1:
            now += speed
            distance += now
        elif plus_minus == 2:
            if now < speed:
                now = 0
            else:
                now -= speed
                distance += now
        else:
            distance += now
       
    print(f'#{test_case} {distance}')
            
        
        