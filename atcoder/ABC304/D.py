W, H = map(int, input().split())
N = int(input())
strawberries = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

cake = [[0 for _ in range(H+1)] for _ in range(W+1)]

for strawberry in strawberries:
    x, y = strawberry
    cake[x][y] += 1

a = [0] + a + [W]
b = [0] + b + [H]

counts = []
for i in range(len(a)-1):
    for j in range(len(b)-1):
        count = 0
        for x in range(a[i], a[i+1]):
            for y in range(b[j], b[j+1]):
                count += cake[x][y]
        counts.append(count)

print(min(counts), max(counts))
