import sys
import itertools

input = sys.stdin.readline
N = int(input())

for _ in range(N):
    
    lst = list(map(int, input().split()))
    gcd = 0
    lst = lst[1:]
    for value in itertools.combinations(lst, 2):
        i, j = value
        for k in range(min(i,j), 0, -1):
            if i%k == 0 and j%k == 0:
                gcd += k
                break
    print(gcd)
