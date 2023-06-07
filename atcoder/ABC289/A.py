n = input()
tmp = ""
res = ""

for v in n:
    if v == "0":
        tmp = "1"
    else:
        tmp = "0"

    res += tmp

print(res)
