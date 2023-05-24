import sys
import math
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
str1_ = ""
str2_ = ""

while True:
    if len(str1_) == math.lcm(len(str1),len(str2)):
        break
    else:
        str1_ += str1
    
while True:
    if len(str2_) == math.lcm(len(str1),len(str2)):
        break
    else:
        str2_ += str2
    
    
if str1_ != str2_:
    print(0)

else:
    print(1)