import sys
import math
input = sys.stdin.readline

s = input().rstrip()
lst = []

for i in range(len(s)):
    lst.append(s[i:])

lst.sort()

for l in lst:
    print(l)
