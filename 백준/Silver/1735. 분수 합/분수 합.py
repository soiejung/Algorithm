import sys
import itertools
import math
input = sys.stdin.readline
bunja = []
bunmo = []

    
for _ in range(2):
    
    A , B = map(int,input().split())
    bunja.append(A)
    bunmo.append(B)

bunja[0] *= math.lcm(bunmo[0],bunmo[1])//bunmo[0]
bunja[1] *= math.lcm(bunmo[0],bunmo[1])//bunmo[1]

bunja_ = bunja[0]+bunja[1]
bunmo_ = math.lcm(bunmo[0],bunmo[1])

bunja_1 = bunja_ // math.gcd(bunja_,bunmo_)
bunmo_1 = bunmo_ // math.gcd(bunja_,bunmo_)
print(bunja_1,bunmo_1)
    
