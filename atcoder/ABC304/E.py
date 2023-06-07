import sys
input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
xy = [list(map(int, input().split())) for _ in range(K)]
Q = int(input())
pq = [list(map(int, input().split())) for _ in range(Q)]

uf = UnionFind(N + 1)
for u, v in edges:
    uf.union(u, v)

for p, q in pq:
    uf.union(p, q)
    for x, y in xy:
        if uf.find(x) == uf.find(y):
            print('No')
            break
    else:
        print('Yes')
