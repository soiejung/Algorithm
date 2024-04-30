def solution(nums):
    answer = 0
    n = len(nums)
    snums = set(nums)
    if len(snums) < int(n/2):
        answer = len(snums)
    else:
        answer = int(n/2)
    return answer