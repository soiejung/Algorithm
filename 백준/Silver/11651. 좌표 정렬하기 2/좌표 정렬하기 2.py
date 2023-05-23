import sys
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    
    x, y = map(int, input().split())
    lst.append([x,y])
    
lst.sort(key= lambda x : (x[1],x[0]))

for l in lst:
    print(l[0],l[1])