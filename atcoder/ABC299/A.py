import sys

n = int(input())
s = input()
star_index = s.index("*")

if "|" not in s[:star_index]:
    print("out")
    exit()

if "|" not in s[star_index+1:]:
    print("out")
    exit()

print("in")
