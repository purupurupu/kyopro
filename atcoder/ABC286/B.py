import re

N = int(input())
S = input()

tmp = re.sub("na", "nya", S)
print(tmp)
