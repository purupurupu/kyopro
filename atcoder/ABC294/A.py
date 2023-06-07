import sys

n = int(input())
s = input()

check = s[0]

for i in range(1, n):
    if s[i] == check:
        print("No")
        sys.exit()
    else:
        check = s[i]

print("Yes")
