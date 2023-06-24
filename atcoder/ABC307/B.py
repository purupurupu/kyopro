def is_palindrome(s):
    return s == s[::-1]


N = int(input())
strings = []
for _ in range(N):
    strings.append(input())

res = False
for i in range(N):
    for j in range(N):
        if i != j and is_palindrome(strings[i] + strings[j]):
            res = True
            break
    if res:
        break

if res:
    print("Yes")
else:
    print("No")
