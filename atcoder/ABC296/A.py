N = int(input())
num_list = list(map(int, input().split()))  # n個の数字がリストに格納される

for i in num_list:
    if i % 2 == 0:
        print(i, end=' ')

# print(s.upper())
