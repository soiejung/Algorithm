
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    num = int(input())
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0
    
    while True:
        if num == 1:
            break
        else:
            if num%2==0:
                a_count += 1
                num = num/2
            if num %3 == 0:
                b_count += 1
                num = num / 3
            if num % 5 == 0:
                c_count += 1
                num = num/5
            if num % 7 == 0:
                d_count += 1
                num = num / 7
            if num % 11 == 0:
                e_count += 1
                num = num/11
      
    print(f'#{test_case} {a_count} {b_count} {c_count} {d_count} {e_count}')