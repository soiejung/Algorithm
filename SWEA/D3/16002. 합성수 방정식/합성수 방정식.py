import math
 
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
 
T = int(input())
for test_case in range(1,T+1):
    x = 3
    n = int(input())
    while True:
        if not is_prime(x) and not is_prime(x+n):
            print(f'#{test_case} {x+n} {x}')
            break
        x +=1