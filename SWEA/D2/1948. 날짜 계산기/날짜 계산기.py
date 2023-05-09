T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    m1,d1,m2,d2 = map(int, input().split())
    sum_=0
    
    if m1 == m2:
        sum_ = d2 - d1 + 1
    else:
        for i in range(m1, m2-1):
            sum_+=month[i]
        sum_ += month[m1-1] - d1 + 1
        sum_ += d2
        
    print(f'#{test_case} {sum_}')