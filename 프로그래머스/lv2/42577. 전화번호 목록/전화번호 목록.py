def solution(phone_book):
    answer = True
    size = len(phone_book)
    hashDict={}
    
    for i in phone_book:
        hashDict[i] = 1
    
    for number in phone_book:
        jubdoo= ""  
        for k in number:
            jubdoo+=k

            if jubdoo in hashDict and jubdoo !=number:
                answer = False

      
    return answer