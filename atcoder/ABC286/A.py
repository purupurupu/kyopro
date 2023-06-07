import copy

n, p, q, r, s = map(int, input().split())
num_list = list(map(int, input().split()))  # n個の数字がリストに格納される

num_list_res = copy.deepcopy(num_list)  # 変更行

diff = r-p

# print(num_list[p-1:q])
# print(num_list[r-1:s])

for i in range(n):
    if i >= p-1 and i <= q-1:
        num_list_res[i] = num_list[i+diff]
        num_list_res[i+diff] = num_list[i]

print(" ".join(map(str, num_list_res)))

# print(num_list_res)
