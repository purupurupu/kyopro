from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visited = [False] * N
components = []
for v in range(N):
    if not visited[v]:
        q = deque([v])
        visited[v] = True
        component = []
        while q:
            u = q.popleft()
            component.append(u)
            for nv in graph[u]:
                if not visited[nv]:
                    q.append(nv)
                    visited[nv] = True
        components.append(component)

for component in components:
    num_vertices = len(component)
    num_edges = sum(len(graph[v]) for v in component) // 2
    if num_vertices != num_edges:
        print("No")
        break
else:
    print("Yes")
