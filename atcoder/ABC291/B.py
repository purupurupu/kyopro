n = int(input())
num_list = list(map(int, input().split()))

sort_list = sorted(num_list)
# print(sort_list)


for i in range(n):
    sort_list = sort_list[1:len(sort_list)-1]
    # print(sort_list)

res = sum(sort_list)/len(sort_list)

print(res)
