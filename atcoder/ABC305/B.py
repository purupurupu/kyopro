p, q = input().split()

points = {'A': 0, 'B': 3, 'C': 4, 'D': 8, 'E': 9, 'F': 14, 'G': 23}

res = abs(points[p] - points[q])

print(res)
