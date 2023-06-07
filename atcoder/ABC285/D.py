import sys

N = int(input())
d = {}
# dd = {}
flag = False

for i in range(N):
    a, b = input().split()
    d[a] = b

# print(d)
for k in d:
    search = d[k]  # init
    dd = {}

    while flag == False:
        if search in d:
            if search in dd:
                print("No")
                sys.exit()

            dd[k] = d[k]
            search = d[search]
            continue

        else:
            break


print("Yes")
