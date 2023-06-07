from collections import defaultdict


def solve(N, edges):
    deg = defaultdict(int)
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    levels = [d for d in deg.values() if d > 1]
    levels.sort()
    return levels


N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]
levels = solve(N, edges)
print(' '.join(map(str, levels)))
