H, W = map(int, input().split())

S = []
T = []

count = 0
new_str_list = ""

for _ in range(H):
    new_str_list = sorted(input())
    new_str = ''.join(new_str_list)
    S.append(new_str)

for _ in range(H):
    new_str_list = sorted(input())
    new_str = ''.join(new_str_list)
    T.append(new_str)

for i in range(H):
    if S[i] == T[i]:
        count += 1

if count == H:
    print("Yes")

else:
    print("No")
