H, W = map(int, input().split())
# print(H, W)
s = ""
for i in range(H):
    s += input()

print(s.count("#"))
