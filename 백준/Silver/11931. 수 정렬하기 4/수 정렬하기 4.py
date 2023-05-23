import sys
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
    
lst.sort(reverse = True)

for i in range(len(lst)):
    print(lst[i])