import sys

n, a, b = map(int, input().split())
s = input()
cost = 0
flag = False

if s == s[::-1]:
    print(cost)
    sys.exit()

act_a = s[1:n] + s[0]
print(act_a)

while flag == False:
    act_a = s[1:n] + s[0]
    if act_a == act_a[::-1]:
        print(cost + a)

    else:
        for i in range(n//2):
