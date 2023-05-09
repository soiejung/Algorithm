T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if a> b:
        a , b = b, a
        A, B = B, A
    result = []

    for i in range(b-a+1):
        sum_ = 0
        for j in range(a):       
            sum_ += (A[j] * B[i+j])
        result.append(sum_)
        
    print(f'#{test_case} {max(result)}')