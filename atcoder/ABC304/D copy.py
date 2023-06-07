W, H = map(int, input().split())
N = int(input())
strawberries = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
a = [0] + list(map(int, input().split())) + [W]
B = int(input())
b = [0] + list(map(int, input().split())) + [H]

# Count strawberries in each segment
segments = [[0]*(len(b)-1) for _ in range(len(a)-1)]
for x, y in strawberries:
    for i in range(len(a)-1):
        if a[i] <= x < a[i+1]:
            for j in range(len(b)-1):
                if b[j] <= y < b[j+1]:
                    segments[i][j] += 1
                    break
            break

min_strawberries = min(min(row) for row in segments)
max_strawberries = max(max(row) for row in segments)

print(min_strawberries, max_strawberries)
