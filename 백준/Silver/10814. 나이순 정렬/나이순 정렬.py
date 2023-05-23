import sys
input = sys.stdin.readline
N = int(input())
lst = []
for n in range(N):
    
    age, name = input().split()
    age = int(age)
    lst.append([age, name, n])

lst.sort(key=lambda x: (x[0], x[2]))

for l in lst:
    print(l[0], l[1])