T = int(input())
for test_case in range(1, T + 1):
    list_ = input()
    lst_1 = []
    for k in range(1,10):
        if list_[:k] == list_[k:2*k]:
            print(f'#{test_case} {k}')
            break
