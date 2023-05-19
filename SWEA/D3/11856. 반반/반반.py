
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    lst = list(input())
    lst_set = set(lst)
    count_lst = []
    for l in lst_set:
        count = lst.count(l)
        count_lst.append(count)
    
    flag = 1
    for c in count_lst:
        if c != 2:
            flag = 0
            break
            
    if flag:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')
