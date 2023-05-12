
from itertools import *

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    num = list(input())
    target = [i for i in range(len(num))]
    num_min, num_max = int(''.join(num)), int(''.join(num))
    
    for value in combinations(target, 2):
        i, j = value
        num[i], num[j] = num[j], num[i]
        if num[0] == '0':
            num[i], num[j] = num[j],num[i]
            continue
                   
        if int(''.join(num)) < num_min:
                   num_min = int(''.join(num))
        if int(''.join(num)) > num_max:
                   num_max = int(''.join(num))
                
        num[i],num[j] = num[j], num[i]
    print(f'#{test_case} {num_min} {num_max}')
        