import sys

input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()
lst = []

for S in s:
    lst.append(S)
    if ''.join(lst[-len(bomb):]) == bomb:
        del lst[-len(bomb):]

lst = ''.join(lst)
if not lst:
    print("FRULA")
else:
    print(lst)