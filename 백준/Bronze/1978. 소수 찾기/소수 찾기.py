import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))

count = 0
for l in lst:
    flag = 1
    if l != 1:
        for i in range(2,l):
            if l % i == 0:
                flag = 0
                break
    
    else:
        flag = 0
        
    if flag:
        count += 1
    

print(count)