def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        check = phone_book[i]
        for j in range(i+1,len(phone_book)):
            if check not in phone_book[j]:
                break
            else:
                if phone_book[j][:len(check)] == check:
                    return False
    
    return answer