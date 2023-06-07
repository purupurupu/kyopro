# S = int(input())
# length = len(str(S))
# print(length)

import sys

S = input()
length = len(S)
res = 0


if length == 1:
    print(1)
    sys.exit()

if length == 2:
    print(2)
    sys.exit()

i = 0

while i < length:
    if S[i] != "0":
        res += 1
        i += 1
        continue

    if i + 1 <= length - 1:
        if S[i] == "0" and S[i+1] == "0":
            res += 1
            i += 2
            continue

    if S[i] == "0":
        res += 1
        i += 1
        continue

print(res)
