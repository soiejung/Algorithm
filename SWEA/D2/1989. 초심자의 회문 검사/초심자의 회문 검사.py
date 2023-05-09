
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str_ = input()
    list_ = []
    
    for i in range(len(str_)-1, -1, -1):
        list_.append(str_[i])
        
    for s in str_:
        if list_:
            if s == list_[0]:             
                list_.pop(0)
                
            else:
                break

    if list_:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')
        
    
