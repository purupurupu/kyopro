n, a, b = map(int, input().split())
c = list(map(int, input().split()))  # n個の数字がリストに格納される

sum = a + b

for i, c in enumerate(c):
    if sum == c:
        print(i+1)
        break
