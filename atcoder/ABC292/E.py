import heapq

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
in_degree = [0] * n
for _ in range(m):
    x, y = map(int, input().split())
    edges[x - 1].append(y - 1)
    in_degree[y - 1] += 1

heap = []
for i in range(n):
    if in_degree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    node = heapq.heappop(heap)
    result.append(node)
    for neighbor in edges[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            heapq.heappush(heap, neighbor)

if len(result) == n:
    a = [0] * n
    for i in range(n):
        a[result[i]] = i + 1
    print("Yes")
    print(" ".join(str(x) for x in a))
else:
    print("No")
