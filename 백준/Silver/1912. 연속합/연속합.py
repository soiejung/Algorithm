import sys
#sys.stdin = open("복습/input.txt","r")
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
total = [0 for _ in range(n+1)]

for i in range(n):

    total[i+1] = max(total[i]+lst[i],lst[i])


print(max(total[1:]))