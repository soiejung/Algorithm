T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    num = input()
    year_ = num[:4]
    month_ = num[4:6]
    date_ = num[6:]
    
    if month_ < '01' or month_ > '12':
        print(f'#{test_case} -1')
        
    elif month_ == '01' or month_ == '03' or month_ == '05' or month_ == '07' or month_ == '08' or month_ == '10' or month_ == '12':
        if date_ <' 00' or date_ > '31':
            print(f'#{test_case} -1')
        else:
            print(f'#{test_case} {year_}/{month_}/{date_}')
            
    elif month_ == '02':
        if date_ <' 00' or date_ > '28':
            print(f'#{test_case} -1')
        else:
            print(f'#{test_case} {year_}/{month_}/{date_}')
    else:
        if date_ < '00' or date_ > '30':
            print(f'#{test_case} -1')
        else:
            print(f'#{test_case} {year_}/{month_}/{date_}')
            
        
        
    # ///////////////////////////////////////////////////////////////////////////////////
