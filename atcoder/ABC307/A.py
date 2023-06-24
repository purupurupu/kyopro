n = int(input())
num_list = list(map(int, input().split()))

res = []

for i in range(n):
    start = i * 7
    end = start + 7
    tmp = sum(num_list[start:end])
    res.append(tmp)

for i in res:
    print(i, end=" ")

# print(res)
