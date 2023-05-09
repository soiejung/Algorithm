dic = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/' ]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    list_ = list(input())
    bin_ = ''
    result = ''
    for l in list_:
        en = dic.index(l)
        list_b = str(bin(en)[2:])
        while len(list_b) < 6:
            list_b = '0' + list_b
        
        bin_ += list_b

    for i in range(len(list_) * 6//8):
        int_ = int(bin_[i*8:i*8+8], 2)
        result += chr(int_)
        
    print(f'#{test_case} {result}')
        
    
    