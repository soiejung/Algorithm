import sys
input = sys.stdin.readline

u = int(input().rstrip())
v = int(input().rstrip())
graph = [[0 for _ in range(u+1)] for _ in range(u+1)]
visited = [0]*(u+1)

def dfs(start):

    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

for _ in range(v):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

dfs(1)
print(visited[1:].count(1)-1)
