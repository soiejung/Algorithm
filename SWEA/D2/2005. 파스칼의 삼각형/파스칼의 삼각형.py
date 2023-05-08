

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case}')
    N = int(input())
    triangle = []
    for i in range(N):
        list_ = []
        for k in range(i+1):
            if k == 0 or k == i:
                list_.append(1)
            else:
                list_.append(triangle[i-1][k] + triangle[i-1][k-1])
        triangle.append(list_)
    for i in triangle:
        print(*i)
