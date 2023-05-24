import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

count = 0
while True:
    try:
        idx = str1.index(str2)
        str1 = str1[idx+len(str2):]
        count += 1
    except ValueError:
        break

print(count)