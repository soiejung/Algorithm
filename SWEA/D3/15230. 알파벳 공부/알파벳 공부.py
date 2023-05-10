alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    lst = list(input())
    
    count = 0
    
    for i in range(len(lst)):
        if lst[i] == alphabet[i]:
            count+=1
        else:
            break
    
    print(f'#{test_case} {count}')
