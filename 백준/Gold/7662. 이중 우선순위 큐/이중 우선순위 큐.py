import sys
input = sys.stdin.readline
import heapq
T = int(input().rstrip())

for test_case in range(T):

    k = int(input().rstrip())
    max_heap = [] # 리스트 썼을 때 시간초과나서 deque로 바꿈, deque도 시간초과!
    min_heap=[]
    visited = [False] * k
    # 최대 최소 구하는데 빠른 heap으로 해봄
    for i in range(k):
        c, n = input().split()
        n = int(n)
        if c == 'I':
            heapq.heappush(max_heap, (-n,i))
            heapq.heappush(min_heap, (n, i))
            visited[i] = True
        elif c == 'D':

            if n == 1:

                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
                '''heap = heapq.nlargest(len(heap), heap)[1:]
                # 큰 숫자 순서대로 가져와서 맨 앞 제외하고 슬라이싱
                # 시간초과 ㅠㅠ
                heapq.heapify(heap)
                # 최소 힙으로 만듦'''

            elif n == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # max_heap과 min_heap 동기화 하기 위해 visited가 False인 요소들 없애주기
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)


    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")


