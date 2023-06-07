n = int(input())
s = input()

init = -1
count = 0
max_count = 0
for i in range(n):
    if s[i] == "-":
        for j in range(i, n):
            if s[j] == "o":
                count += 1
                if max_count < count:
                    max_count = count
            else:
                if max_count < count:
                    max_count = count
                count = 0

s_reverse = s[::-1]
count = 0
for i in range(n):
    if s_reverse[i] == "-":
        for j in range(i, n):
            if s_reverse[j] == "o":
                count += 1
                if max_count < count:
                    max_count = count
            else:
                if max_count < count:
                    max_count = count
                count = 0

if max_count == 0:
    print(init)
else:
    print(max_count)
