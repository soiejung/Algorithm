import sys
input = sys.stdin.readline

n, m = input().split()

A = set(map(int,input().split()))
B = set(map(int, input().split()))
r1 = A - A.intersection(B)
r2 = B - B.intersection(A)
result = r1.union(r2)

print(len(result))