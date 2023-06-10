n = int(input())

tmp = n % 5
tmp2 = n // 5
if tmp >= 3:
    res = tmp2 * 5 + 5
else:
    res = tmp2 * 5

print(res)
