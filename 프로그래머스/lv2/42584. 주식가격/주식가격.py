def solution(prices):
    answer = []

    for i in range(len(prices)):
        min = prices[i]
        count = 0
        for k in range(i+1, len(prices)):
            if prices[i] <= prices[k]:
                count+=1
            else:
                count+=1
                break
        answer.append(count)
    return answer