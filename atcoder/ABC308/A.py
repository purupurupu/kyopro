s_list = list(map(int, input().split()))

tmp_sort = sorted(s_list)

if s_list != tmp_sort:
    print("No")
    exit()

for i, c in enumerate(s_list):
    if c >= 100 and c <= 675 and c % 25 == 0:
        continue
    else:
        print("No")
        exit()

print("Yes")
