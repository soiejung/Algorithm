
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N = int(input())
    day = list(map(int,input().split()))
    cnt_list = []
    for a in range(7):
        
        count = 0
        day_count = 0
        b = a  
        while count < N:
            if day[b] == 1:
                count += 1
            b+=1
            day_count += 1
            
            if b == 7:
                b = 0
        cnt_list.append(day_count)
           
    print(f'#{test_case} {min(cnt_list)}')
        
        
        