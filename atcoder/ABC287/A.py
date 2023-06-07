n = int(input())
str_list = [input() for _ in range(n)]

count = str_list.count("For")
if count > n / 2:
    print("Yes")
else:
    print("No")
