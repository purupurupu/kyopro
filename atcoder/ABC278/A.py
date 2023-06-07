n, k = input().split()
num_list = list(map(int, input().split()))  # n個の数字がリストに格納される

for i in range(int(k)):
    num_list.pop(0)
    num_list.append(0)

for v in num_list:
    print(v, end=' ')
