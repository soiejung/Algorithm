T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    list_ = list(map(int, input().split()))
    max_ = max(list_)
    min_ = min(list_)
    sum_ = 0
    answer = 0
    for l in list_:
        sum_ += l
    sum_ -= max_
    sum_ -= min_
    
    answer = round(sum_/(len(list_)-2))
    print(f'#{test_case} {answer}')