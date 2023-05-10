
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    lst = input()
    count = 0
    for i in range(len(lst)):
        if i < len(lst)-1 and lst[i] ==  '(':
            if lst[i+1] == '|' or lst[i+1] == ')':
                count += 1
        elif i > 0 and lst[i] == ')':
            if lst[i-1] == '|':
                count += 1
    
    print(f'#{test_case} {count}')
            