N = int(input())
num = list(map(str,range(1,N+1)))
for n in num:
    if '3' in n or '6' in n or '9' in n:
        for i in range(len(n)):
            if n[i] == '3' or n[i] == '6' or n[i] == '9':
                print('-', end= '')
        print('',end=' ')
    else:
        print(n, end= ' ')

