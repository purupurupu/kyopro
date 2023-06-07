import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


def dfs(u, v, graph, visited):
    stack = [u]
    while stack:
        node = stack.pop()
        if node == v:
            return True
        if not visited[node]:
            visited[node] = True
            stack.extend(graph[node])
    return False


N, M = map(int, input().split())
edges = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

K = int(input())
constraints = [tuple(map(int, input().split())) for _ in range(K)]

Q = int(input())
questions = [tuple(map(int, input().split())) for _ in range(Q)]

for p, q in questions:
    # Add new edge for the question
    edges[p].append(q)
    edges[q].append(p)
    for x, y in constraints:
        visited = [False] * (N+1)
        if dfs(x, y, edges, visited):
            print('No')
            break
    else:
        print('Yes')
    # Remove the new edge after the question
    edges[p].remove(q)
    edges[q].remove(p)
