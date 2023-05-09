def oman(money):
    if money // 50000:
        unit = money//50000
        return unit
def man(money):
    if money // 10000:
        unit = money//10000
        return unit
def ochun(money):
    if money // 5000:
        unit = money//5000
        return unit
def chun(money):
    if money // 1000:
        unit = money//1000
        return unit
    
def obaek(money):
    if money // 500:
        unit = money//500
        return unit
    
def baek(money):
    if money // 100:
        unit = money//100
        return unit
    
def osip(money):
    if money // 50:
        unit = money//50
        return unit
    
def sip(money):
    if money // 10:
        unit = money//10
        return unit
    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    money_str = input()
    money = int(money_str)
    unit = [0] * 8
    if oman(money):
        unit[0] = oman(money)
        money -= unit[0]*50000
    if man(money):
        unit[1] = man(money)
        money -= unit[1]*10000
    if ochun(money):
        unit[2] = ochun(money)
        money -= unit[2]*5000
    if chun(money):
        unit[3] = chun(money)
        money -= unit[3] * 1000
    if obaek(money):
        unit[4] = obaek(money)
        money -= unit[4] * 500
    if baek(money):
        unit[5] = baek(money)
        money -= unit[5] * 100
    if osip(money):
        unit[6] = osip(money)
        money -= unit[6] * 50
    if sip(money):
        unit[7] = sip(money)
        money -= unit[7] * 10
           
    print(f'#{test_case}')
    for u in unit:
        print(u, end= ' ')
    print('')