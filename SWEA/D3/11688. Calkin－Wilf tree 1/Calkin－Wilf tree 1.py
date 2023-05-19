
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    move = list(input())
    a =1
    b =1
    for i in range(len(move)):
        if move[i] == 'L':
            a = a
            b = a + b
        elif move[i] == 'R':
            a = a+b
            b = b
            
    print(f'#{test_case} {a} {b}')
