from re import I
import sys

S = input()

d = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}

length = len(S)
rev = S[::-1]

res = 0
# print(rev)

for i in range(length):
    if i == 0:
        res = d[rev[i]]
        continue
    res = res + d[rev[i]] * 26 ** i

print(res)
