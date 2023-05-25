import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

def dfs(start, depth):
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)


def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1



for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = 1
        else:
            #dfs(i,0)
            bfs(i)
            count += 1


print(count)
