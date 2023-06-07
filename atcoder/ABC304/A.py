n = int(input())
str_list = []
for i in range(n):
    str_list.append(list(input().split()))
# print(str_list)

name_list = []
age_list = []
for i in str_list:
    name_list.append(i[0])
    age_list.append(int(i[1]))

min_age = min(age_list)
min_age_index = age_list.index(min_age)

res = name_list[min_age_index:] + name_list[:min_age_index]

for name in res:
    print(name)
