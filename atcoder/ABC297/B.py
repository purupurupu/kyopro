import sys

s = input()  # 文字列Sを受け取る
b_indices = [i for i in range(len(s)) if s[i] == "B"]
r_indices = [i for i in range(len(s)) if s[i] == "R"]
k_index = s.index("K")

for i in range(len(b_indices)):
    for j in range(i+1, len(b_indices)):
        if (b_indices[i]+1) % 2 == (b_indices[j]+1) % 2:
            print("No")
            sys.exit()

for i in range(len(r_indices)):
    for j in range(i+1, len(r_indices)):
        if k_index > r_indices[i] and k_index < r_indices[j]:
            print("Yes")
            sys.exit()

print("No")
