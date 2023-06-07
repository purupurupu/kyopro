import heapq
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
l = [0]
s = set()
heapq.heapify(l)
for i in range(K):
    q = heapq.heappop(l)
    for i in A:
        if i+q not in s:
            heapq.heappush(l, i+q)
            s.add(i+q)
print(heapq.heappop(l))
