
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    count = 0
    print(f'#{test_case}')
    for i in range(N):
        char_, num = input().split()
        num = int(num)
        for i in range(num):
            print(char_, end='')
            count += 1
            if count >= 10:
                print()
                count = 0
    print()