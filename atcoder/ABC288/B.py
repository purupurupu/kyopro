n, k = map(int, input().split())
str_list = [input() for _ in range(n)]
tmp = str_list[:k]

tmp = sorted(tmp)
# print(tmp)

for v in tmp:
    print(v)
