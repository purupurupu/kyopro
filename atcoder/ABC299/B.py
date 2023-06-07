n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))


max_value = 0
res = 0
for i in range(n):
    if c[i] == t and r[i] > max_value:
        max_value = r[i]
        res = i+1

if res == 0:
    max_value = 0
    for i in range(n):
        if c[i] == c[0] and r[i] > max_value:
            max_value = r[i]
            res = i+1
print(res)
