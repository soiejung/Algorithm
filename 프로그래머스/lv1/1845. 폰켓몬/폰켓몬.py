def solution(nums):
    answer = 0
    hash = {}
    sizeOfnums = len(nums)
    max = int(sizeOfnums/2)
    for i in nums:
        hash[i] = 1
    count = len(hash.keys())
    if count <= max:
        answer = count
    else:
        answer = max
                
    return answer

    